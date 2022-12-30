from util.util import load_model

def predict(values, model_path):
	clf = load_model(model_path)
	return clf.predict(values)