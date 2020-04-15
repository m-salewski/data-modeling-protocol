#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.preprocessing import OrdinalEncoder

def get_cat_encoding(df, cols_to_encode):
    
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
