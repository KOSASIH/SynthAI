import os

# data paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
TRAINING_DATA_DIR = os.path.join(DATA_DIR, 'training')
TESTING_DATA_DIR = os.path.join(DATA_DIR, 'testing')
GENERATED_DATA_DIR = os.path.join(DATA_DIR, 'generated')

# model paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'model.pkl')

# logging
LOG_DIR = os.path.join(os.path.dirname(__file__), '..', 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'app.log')
