import os
import sys
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Entry point for Data modeling protocol')
    parser.add_argument('Path', type=str, help="Give the path to the dataset")
    return parser.parse_args()