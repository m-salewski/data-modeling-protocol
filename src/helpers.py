import os
import sys
import argparse
import logging
import json




# Setup logging
def setup_logging(config):
    if config["logging"]["enabled"]:
        logging.basicConfig(level=logging.DEBUG)        

def get_config(path_to_config):
    if os.path.exists(path_to_config):
        logging.info(" Reading config")
        with open("config.json", "r") as f:
            config = json.load(f)
            return config
    else:
        raise Exception(f"Problem while trying to read config at {path_to_config}")
        

def get_parser():
    parser = argparse.ArgumentParser(description='Entry point for Data modeling protocol')
    parser.add_argument('Path', type=str, help="Give the path to the dataset")
    path = parser.parse_args().Path

    if os.path.exists(path):
        return path
    else:
        logging.error(f"Problem while reading dataset at {path}")