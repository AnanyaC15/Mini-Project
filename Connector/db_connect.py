import pandas as pd


def pull_data(link: str) -> pd.DataFrame:
    """
    This function extracts data from the github link given below
    """

    df = pd.read_csv(link)
    return df