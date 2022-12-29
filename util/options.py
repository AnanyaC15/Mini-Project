import argparse

def train_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("--parameters", default=100, type=int, help='')
    parser.add_argument("--model", default=100, type=str, help='number of estimators')
    parser.add_argument("--max_features", default=6, type=int, help='maximum of features',)
    parser.add_argument("--max_depth", default=5, type=int,help='maximum depth')
    opt = parser.parse_args()
    return opt