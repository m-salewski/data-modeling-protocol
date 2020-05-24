import pandas as pd
import argparse
import os
import sys
import logging
import json
import seaborn as sns

from helpers import get_parser, setup_logging, get_config
from features import fill_rates

def main(df, config):
    # Target feature selection
    target = config["dataset"]["target_feature"]
    df_targ = df[['id', target]].copy()
    df = df.drop(columns=target).copy()

    # Separate features based on type
    ignore_cols = config["dataset"]["ignore_columns"]
    float_cols = df.drop(columns=ignore_cols).select_dtypes('float').columns.tolist()
    int_cols = df.drop(columns=ignore_cols).select_dtypes('int').columns.tolist()
    num_cols = df.drop(columns=ignore_cols).select_dtypes(['int', 'float']).columns.tolist()
    string_cols = df.drop(columns=ignore_cols).select_dtypes('object').columns.tolist()

    df_fillrates = fill_rates.get_column_fill_rates(df,0.0)
    df_fillrates.sort_values("frac_full", ascending=True).to_csv("../output/fill_rates.csv", index=None)
    unfilled_cols = df_fillrates[df_fillrates['frac_full']<=0.90]['column_name'].tolist()
    colours = ['#000099', '#ffff00'] # specify the colours - yellow is missing. blue is not missing.
    unfilled_plot = sns.heatmap(df[unfilled_cols].isnull().sample(frac=1).reset_index(drop=True), cmap=sns.color_palette(colours)) 
    unfilled_plot.figure.savefig("../output/unfilled_plot.png")


    # Drop based on NAs

    # Drop based on correlation

    
    pass


if __name__ == "__main__":

    get_parser()
    PATH_TO_CONFIG = "config.json"
    config = get_config(PATH_TO_CONFIG)

    setup_logging(config)


    path_to_dataset = config["dataset"]["path"]
    
    df = pd.read_csv(path_to_dataset, infer_datetime_format=True, parse_dates=['timestamp'])

    logging.info("Dataset loaded")  
    logging.info(f"Dataset has the following shape {df.shape}")

    main(df, config)

