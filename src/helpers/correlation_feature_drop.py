#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import operator

from IPython.display import display

def get_correlation_pairs(df_corr, target_feature=None): 
    
    """ Reassembles a square dataframe of correlated features and their correlation coefficients into
     a dataframe of the correlation pairs (2 columns) and their correlation coefficients

    :param df_corr: [DataFrame] (Square) DataFrame of feature correlation coefficients
    :param target_feature: [string] Name of the target feature; it None, assumes that it has been already stripped.
    :return: [DataFrame] The dataframe of the correlation pairs and their correlation coefficients
    """
    
    if target_feature != None:
        # Drop the target variable
        
        df_corr = df_corr.drop(index=target_feature, columns=target_feature)
    
    # Steps
    # 1. reset to get the row feature indices as a new col
    # 2. melt into feature1, feature2, correlation coeff.
    # 3. rename for convenience
    df_cpairs = \
        df_corr\
        .reset_index()\
        .melt(id_vars=['index'], value_vars=df_corr.columns)\
        .rename(columns={'index':'col1','variable':'col2', 'value':'corr'})
    
    return df_cpairs


get_dict = lambda col, targ: dict(zip(col,targ))

get_max_key = lambda dct: max(dct.items(), key=operator.itemgetter(1))[0]

get_rep = lambda  col, targ: get_max_key(dict(zip(col,targ)))

#sorter = lambda set_in : sorted(set_in, key=int)
sorter = lambda set_in : sorted(set_in)

def get_dropped_columns_inner(df_cpairs, replacers,  target_feature, threshold = 0.9, verbose = False):
    
    if verbose: print("Incoming:", len(replacers))
    
    new_replacers = df_cpairs[(df_cpairs.col1.isin(replacers)) & \
                              (df_cpairs.col2.isin(replacers)) & \
                              (df_cpairs['corr'] > threshold) & \
                               df_cpairs['self']]['col1'].unique().tolist()
    
    if verbose: print("Retain:", len(new_replacers))
    
    df_cpairs2 = df_cpairs[(df_cpairs.col1.isin(new_replacers)) & \
                           (df_cpairs.col2.isin(new_replacers)) & \
                           (df_cpairs['corr'] > threshold)]
    
    df_feature_replacer = df_cpairs2[(df_cpairs2['corr']>threshold)]\
        .groupby('col1').apply(lambda x: get_rep(x['col2'],x[target_feature]))\
        .reset_index()\
        .rename(columns={'col1':'feat', 0:'replacer'})
    
    if df_feature_replacer.shape[0] != 0:
        
        features = set(df_feature_replacer.feat.tolist())
        replacers = set(df_feature_replacer.replacer.tolist())
        droppables = features.difference(replacers)
        
        if verbose:
            display(df_cpairs2.round(3).groupby('col1').aggregate({'col2':list,target_feature:list}).reset_index())        
            print("Features:", sorter(features))
            print("Droppables:", sorter(droppables))
            print("Replacements:", sorter(replacers))

        return replacers, droppables
    else:
        return set(), set()

    
def get_dropped_columns_while(df_cpairs, target_feature, threshold, verbose = False):

    test_cols = df_cpairs.col1.unique().tolist()
    
    keepers, droppers = set(),set()
    
    while len(test_cols) != 0:

        replacers, droppables = get_dropped_columns_inner(df_cpairs, test_cols, target_feature, threshold, verbose)
        
        if verbose: print(len(replacers),len(droppables))
        
        keepers.update(replacers)
        droppers.update(droppables)
        test_cols = replacers       
        
    return droppers

def get_dropped_columns(df_corr, target_feature=None, threshold = 0.9, verbose = False):
    
 
    df_cpairs = get_correlation_pairs(df_corr, target_feature)
    print(df_cpairs.columns)    
    df_cpairs['self'] = True
    
    df_cpairs.loc[df_cpairs['col1'] == df_cpairs['col2'],'self'] = False
    
    df_targ_corr = df_corr[target_feature].reset_index().rename(columns={'index':'col2'})
    
    df_cpairs = df_cpairs.merge(df_targ_corr, on='col2', how='inner')
    
    print(df_cpairs.columns)
    
    dropped = get_dropped_columns_while(df_cpairs, target_feature, threshold, verbose)
    
    return list(dropped)