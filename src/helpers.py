import os
import sys
import argparse
import logging
import json




# Setup logging
def setup_logging(config):
    if config["logging"]["enabled"]:
        logging.getLogger().setLevel(logging.INFO)  
        logging.info(" Logging is activated")    

def get_config(path_to_config):
    if os.path.exists(path_to_config):
        logging.info(" Reading config")
        with open("config.json", "r") as f:
            config = json.load(f)
            return config
    else:
        raise Exception(f"Problem while trying to read config at {path_to_config}") 

def get_parser():
    # todo unused - remove?
    parser = argparse.ArgumentParser(description='Entry point for Data modeling protocol', usage=" \n Modify config.json file")
    if len(sys.argv[1:])==0:
        parser.print_help()
    #parser.exit()