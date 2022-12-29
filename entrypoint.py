from models.decisiontrees import predict
from config.conf import logging
from config.conf import settings

prediction = predict(settings.PREDICTION.parameters, model_path=settings.MODEL.dt_conf)
logging.info(f"Prediction: {prediction}")

# # print(f"parameter {settings.DATA.data_set}")

# df = pull_data("https://raw.githubusercontent.com/5x12/ml-cookbook/master/supplements/data/heart.csv")
# X_train, X_test, y_train, y_test = traintest_split(df)
# clf = df_train(X_train, y_train)
# logging.info(f'Accuracy score is: {clf.score(X_test, y_test)}')

# response = predict (X_test)

# logging.info(f'The prediction values are {clf.predict(X_test)}')