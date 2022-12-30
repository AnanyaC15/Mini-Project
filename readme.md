•	PART 1:

Structure of the project

The structure used to build the project:
The following folders contain the related files:

Conf – code supporting files, like our logging and documentation, setting file (.toml) for storing parameters needed by our model, to make the code more robust by using dynamic variables and production ready.

Models – includes all the model related files like training, testing and evaluation. It also has another folder which has the model dump (.pkl files). We have made 3 classifiers namely decision tree, random forest, and logistic regression.

Connector – this folder includes the data source or a db_connect to pull data from the database. In this case we are reading/extracting data from a GitHub link.

Util – utility folder has files with miscellaneous functions supporting our models like storing models and loading it.

Entrypoint.py – this file will help us run the model and get prediction without running each element separately. This file contains our prediction function with the feature values to be used for prediction and path to the model (both parameters coming from settings.toml).

The following libraries have been used to build this project:

	We have used the logging library for the logging each action

	Dynaconf has been used manage our dynamic configurations. All our hardcoded values are stored in a .toml file and therefore we don’t have to go and update our model every time there is a change, or we need to run prediction for new set of values.

	We have used the pickle library to save the model, to minimise lengthy re-training and re-load the pre-trained models whenever needed.

	We have used sklearn to split our datasets, to build the models and run gridsearchCV.

	In the next part of the project, we have also used argparse to run our model and provide feature values from the command line.

Hyperparameters have only been trained for random forest and logistic regression and the one with the highest accuracy is selected and used for prediction.

The file entrypoint will check if the model dump exists under models/conf. If not, it will run the model and then run the prediction function.

To run the prediction model for other 2 models, the model path would need to be updated to the values mentioned in the settings.toml file. 

•	PART 2:

We made another project named multiple_models which can be run from the command line. For this model we use make_classification function to create a classification dataset to work on. The three parameters that need to be inputted for this are:

	Dimensionality reduction techniques - Principal Component Analysis (PCA) or Locally Linear Embedding (LLE)
	Output dimensions (from the dimensionality reduction technique) - 5 and 10 dimensions (as we have a 30-dimensional data).
	Types of Machine Learning Classifier - Logistic Regression, SVC, and Random Forest Classifier.
