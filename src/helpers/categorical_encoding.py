#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OrdinalEncoder

class OrdinalEncoderNans(BaseEstimator, TransformerMixin):
    
    #Class Constructor
    def __init__( self, _cats_to_map):
        self._cats_to_map = _cats_to_map
        
    #Return self, nothing else to do here
    def fit( self, X, y = None ):
        return self 
    
    #Custom transform method we wrote that creates aformentioned features and drops redundant ones 
    def transform(self, X, y = None):
            
        # Map all but the last the categories to ints
        X = X.replace( self._cats_to_map[:-1], np.arange(len(self._cats_to_map[:-1])))
                    
        #Converting any infinity values in the dataset to Nan
        X = X.replace( self._cats_to_map[-1], np.nan )
        
        shape_ = X.shape[0]
        #returns a numpy array
        return X.values


def get_cat_encoding(df, cols_to_encode):
    """
    A more raw version of the above class
    """
    # 1. Copy the data
    # 2. ~~data inspection~~
    #    * deep-dive into some cols
    # 3. ~~select the cols to be transformed~~ --> given
    # 4. Get the encoder; specify the data to encode and transform
    # **Note** this list is specific to this data but it could be passed as argument
    #TODO move to separate function
    categ_list = [['Investment', 'OwnerOccupier']] + [df.sub_area.unique().tolist()] + 12*[['no','yes']]+[['poor', 'satisfactory', 'good', 'excellent', 'no data']]
    
    enc = OrdinalEncoder(categ_list)

    str_enc_data = enc.fit_transform(df[cols_to_encode].values)

    # 5. rewrite encoded to the data
    df[cols_to_encode] = str_enc_data


    # **Note** refill any NANs wished to be retained
    #TODO move to separate function
    encoder_max = df.ecology.max()
    df['ecology'] = np.where(df.ecology==df.ecology.max(), np.NaN, df.ecology)

    # 6. Recast the data, if needed

    df[cols_to_encode[:-1]] = df[cols_to_encode[:-1]].astype('int8')

    # 7. Final check on the data: does it contain all the rows as before?
    # 8. Replace the encoded data (excluded here)

    return df
