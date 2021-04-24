#!/usr/bin/env python
# coding: utf-8

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import io


def get_info(df):
    

    buf = io.StringIO()
    df.info(verbose=True, null_counts=True, buf=buf)
    s = buf.getvalue()

    nr_cols = df.shape[1]
    info_list = s.split('\n')[3:nr_cols+3]

    df_info = pd.DataFrame()
    
    for v in info_list:
        v = v.split()
        dc = {}
        dc['col'] = [v[0]]
        dc['count'] = [int(v[1])]
        dc['type'] = [v[3]]
        #print(dc)
        df_row = pd.DataFrame().from_dict(dc)
        df_info = pd.concat([df_info, df_row])

    df_info.reset_index(drop=True,inplace=True)

    return df_info

