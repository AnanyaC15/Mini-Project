from models.prediction import predict
from config.conf import logging
from config.conf import settings
    
# Check if pkl file exists in models/conf, if not it will run the model. Check the log for message
file_exist (settings.MODEL.lr_conf, logistic_regression)

# Update the model path to run decision tree and random forest. Can be found in the settings file.

prediction = predict(settings.PREDICTION.parameters, model_path=settings.MODEL.rf_conf)
logging.info(f"Prediction: {prediction}")