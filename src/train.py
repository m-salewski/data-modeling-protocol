import pandas as pd
import argparse
import os
import sys
import logging
import json

from helpers import get_parser, setup_logging, get_config

def main(df):
    pass


if __name__ == "__main__":
    PATH_TO_CONFIG = "config.json"
    config = get_config(PATH_TO_CONFIG)

    setup_logging(config)
    
    path_to_dataset = config["dataset"]["path"]
    
    df = pd.read_csv(path_to_dataset, infer_datetime_format=True, parse_dates=['timestamp'])

    logging.info("Dataset loaded")  
    logging.info(f"Dataset has the following shape {df.shape}")

    #main(df)

