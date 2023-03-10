from Connector.db_connect import pull_data
from config.conf import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import pickle
from util.util import store_model, load_model
from models.prediction import predict
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
	clf = LogisticRegression(random_state = 3)
	clf.fit(X_train, y_train)

	#Grid
	parameter_grid = {'C': [0.01, 0.1, 1, 2, 10, 100], 'penalty': ['l1', 'l2']}
	#Gridsearch
	gridsearch = GridSearchCV(clf, parameter_grid)

	# Training the model
	gridsearch.fit(X_train, y_train)
	store_model(loc='models/conf/logistic_reg.pkl', model=gridsearch)
	return gridsearch

df = pull_data(settings.DATA.dataset)

X_train, X_test, y_train, y_test = traintest_split(df)
clf_lr = df_train(X_train, y_train)
logging.info(f'Accuracy score is: {clf_lr.score(X_test, y_test)}')

response = predict(X_test, settings.MODEL.lr_conf)

logging.info(f'The prediction values are {clf_lr.predict(X_test)}')