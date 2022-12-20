from Connector.db_connect import pull_data
from config.log import logging
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def traintest_split(df):
	logging.INFO("Defining X and y")
	# Dividing for the predictors and target variable
	X = df.iloc[:, :-1]
	y = df['target']

	logging.INFO("Splitting the dataset")
	# Split variables into train and test
	X_train, X_test, y_train, y_test = train_test_split(X, #independent variables
													y, #dependent variable
													random_state = 3
												)
	return X_train, X_test, y_train, y_test

def df_train(X_train, y_train):
	logging.INFO("Building and training the model")
	# Building the model
	clf = DecisionTreeClassifier(max_depth = 3, random_state = 3)
	# Training the model
	clf.fit(X_train, y_train)

	return clf

df = pull_data("https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/heart.csv")
X_train, X_test, y_train, y_test = traintest_split(df)
clf = df_train(X_train, y_train)

logging.INFO(f'Accuracy score is: {clf.score(X_test, y_test)}')