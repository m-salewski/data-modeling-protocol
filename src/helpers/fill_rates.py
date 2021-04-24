#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import operator

def get_column_fill_rates(df, threshold=0.0):
    
    
    """ Return a pd.DF with the fill rates of columns in a data frame
    
    Compute the fill rates of a given DF and export the DF 
    with colunms above a given threshold.
    
    Args:    
        df    (pd.DataFrame): input DF
        threshold     float): the lowest fraction of acceptable missing entries
    
    Returns: 
        pd.DataFrame: A DF with features and their fill rates 
        (when above the threshold)

    Raises:
        None

    Examples:
        >>> df.shape
        1000,1000
        >>> df_fill_rates = get_fill_rates(df, 0.10)
        >>> df_fill_rates
        
    """    
    
    ### NOTE: this was for 'missing' values as     
    #         `fill_rates = [(c, df[c].isna().mean()) for c in df]`
    
    fill_rates = [(col, 1.0 - df[col].isna().mean()) for col in df]
    
    df_fill_rate = pd.DataFrame(fill_rates, columns=['column_name', 'frac_full'])
    df_fill_rate = df_fill_rate[df_fill_rate.frac_full >= threshold]
    
    return df_fill_rate


def get_row_fill_rates(df, threshold=0.0):
    
    
    """ Return a pd.DF with the fill rates of columns in a data frame
    
    Compute the fill rates of a given DF and export the DF 
    with colunms above a given threshold.
    
    Args:    
        df    (pd.DataFrame): input DF
        threshold     float): the lowest fraction of acceptable missing entries
    
    Returns: 
        pd.DataFrame: A DF with features and their fill rates 
        (when above the threshold)

    Raises:
        None

    Examples:
        >>> df.shape
        1000,1000
        >>> df_fill_rates = get_fill_rates(df, 0.10)
        >>> df_fill_rates
        
    """    
    
    ### NOTE: this was for 'missing' values as     
    #         `fill_rates = [(c, df[c].isna().mean()) for c in df]`
    
    
    df_fill_rate = df.count(axis=1).reset_index() \
           .rename(columns={'index':'id', 0:'row_counts'})
    nr_of_cols = df.shape[1]
    df_fill_rate['frac_full'] = df_fill_rate \
                            .row_counts.apply(lambda x: x/nr_of_cols)
    
    df_fill_rate = df_fill_rate[df_fill_rate.frac_full >= threshold]
    
    return df_fill_rate