import pandas as pd
from config.conf import logging


def pull_data(link: str) -> pd.DataFrame:
    """
    This function extracts data from the github link given below
    """
    logging.info("Pulling the dataset")
    df = pd.read_csv(link)
    logging.info("Data Extracted")
    return df