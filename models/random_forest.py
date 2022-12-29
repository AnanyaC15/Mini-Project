from Connector.db_connect import pull_data
from config.conf import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
from util.util import store_model, load_model
from config.conf import settings


def traintest_split(df):
	logging.info("Defining X and y")
	# Dividing for the predictors and target variable
	X = df.iloc[:, :-1]
	y = df['target']

	logging.info("Splitting the dataset")
	# Split variables into train and test
	X_train, X_test, y_train, y_test = train_test_split(X, #independent variables
													y, #dependent variable
													random_state = 3
												)
	return X_train, X_test, y_train, y_test

def df_train(X_train, y_train):
	logging.info("Building and training the model")
	# Building the model
	clf = RandomForestClassifier(max_depth = 2, random_state = 0)
	# Training the model
	clf.fit(X_train, y_train)
	store_model(loc='models/conf/random_forest.pkl', model=clf)
	return clf

def predict(values, model_path):
	clf = load_model(model_path)
	return clf.predict(values)

df = pull_data(settings.DATA.dataset)

X_train, X_test, y_train, y_test = traintest_split(df)
clf = df_train(X_train, y_train)
logging.info(f'Accuracy score is: {clf.score(X_test, y_test)}')

response = predict(X_test, settings.MODEL.dt_conf)

logging.info(f'The prediction values are {clf.predict(X_test)}')