#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# from https://chrisalbon.com/machine_learning/feature_selection/drop_highly_correlated_features/
# also seen in https://stackoverflow.com/questions/29294983/how-to-calculate-correlation-between-all-columns-and-remove-highly-correlated-on
def get_corr_feature_drop_1(df_corr,threshold=0.95):

    # Create correlation matrix, with abs since interested only in magnitude
    #df_corr = df.corr().abs()

    # Select upper triangle of correlation matrix
    upper = df_corr.where(np.triu(np.ones(df_corr.shape), k=1).astype(np.bool))

    # Find index of feature columns with correlation greater than threshold
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

    # Drop features 
    #df.drop(to_drop, axis=1, inplace=True)

    return to_drop


# From: https://stackoverflow.com/questions/29294983/how-to-calculate-correlation-between-all-columns-and-remove-highly-correlated-on
def get_corr_feature_drop_2(df_corr, threshold=0.95):

    col_corr = set() # Set of all the names of deleted columns
    #df_corr = df.corr()
    
    
    to_drop = []
    for i in range(len(df_corr.columns)):
        for j in range(i):
            if (df_corr.iloc[i, j] >= threshold) and \
               (df_corr.columns[j] not in col_corr):
                
                colname = df_corr.columns[i] # getting the name of column
                col_corr.add(colname)
                
                #if colname in df.columns:
                if colname in df_corr.columns:
                    to_drop.append(colname)
                    #del df[colname] # deleting the column from the df

    return to_drop


# From: https://stackoverflow.com/questions/29294983/how-to-calculate-correlation-between-all-columns-and-remove-highly-correlated-on
def get_corr_feature_drop_3(df_corr, threshold=0.95):

    '''
    Obj: Drops features that are strongly correlated to other features.
          This lowers model complexity, and aids in generalizing the model.
    Inputs:
          df: features df
          threshold: Columns are dropped relative to the threshold input (e.g. 0.8)
    Output: df that only includes uncorrelated features
    '''

    # Creates Correlation Matrix and Instantiates
    #df_corr = df.corr()
    iters = range(len(df_corr.columns) - 1)
    drop_cols = []

    # Iterates through Correlation Matrix Table to find correlated columns
    for i in iters:
        for j in range(i):
            item = df_corr.iloc[j:(j+1), (i+1):(i+2)]
            col = item.columns
            row = item.index
            val = item.values
            print
            if abs(val) >= threshold:
                # Prints the correlated feature set and the corr val
                #print(col.values[0], "|", row.values[0], "|", round(val[0][0], 2))
                drop_cols.append(col.values[0])

    to_drop = list(set(drop_cols))#[::-1]

    # Drops the correlated columns
    '''for i in drops:
        col = df.iloc[:, (i+1):(i+2)].columns.values
        df = df.drop(col, axis=1)
    '''    
    
    return to_drop

