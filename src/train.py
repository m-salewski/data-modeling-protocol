import pandas as pd
import argparse
import os
import sys

from helpers import get_parser   

def main(dataframe):

    # Tranformation functions

    # 
    pass


if __name__ == "__main__":


    args = get_parser()
    #"../datasets/sberbank-russian-housing-market/train.csv"


    
    df = pd.read_csv(args.path, infer_datetime_format=True, parse_dates=['timestamp'])
    
    main(df)

