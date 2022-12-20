from Connector.db_connect import pull_data
from config.log import logging

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

logging.INFO("Pulling the dataset")
df = pull_data("https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/heart.csv")
print(df)
logging.INFO("Data Extracted")

def train_test_split(df):

	# Dividing for the predictors and target variable
	X = df.iloc[:, :-1]
	y = df['target']

	# Split variables into train and test
	X_train, X_test, y_train, y_test = train_test_split(X, #independent variables
													y, #dependent variable
													random_state = 3
												)
	return X_train, X_test, y_train, y_test

def df_train(X_train, y_train):
	# Building the model
	clf = DecisionTreeClassifier(max_depth = 3, random_state = 3)
	# Training the model
	clf.fit(X_train, y_train)

	return clf