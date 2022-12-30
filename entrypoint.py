from models.prediction import predict
from config.conf import logging
from config.conf import settings
from util.file_check import file_exist
    
# Check if pkl file exists in models/conf, if not it will run the model and create a file under models/cpnf. Check the log for message.
file_exist (settings.MODEL.dt_conf)

# Update the model path to run decision tree and random forest. Can be found in the settings file.

prediction = predict(settings.PREDICTION.parameters, model_path=settings.MODEL.lr_conf)
logging.info(f"Prediction: {prediction}")