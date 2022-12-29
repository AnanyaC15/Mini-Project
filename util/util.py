import pickle

def store_model(loc: str, model) -> None:
    pickle.dump(model, open(loc, "wb"))

def load_model(loc: str) -> None:
    return pickle.load(open(loc, 'rb'))