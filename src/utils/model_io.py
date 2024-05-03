import joblib

def load_model(model_path: str) -> object:
    """
    Load a model from disk.

    Args:
        model_path (str): The path to the model file.

    Returns:
        object: The loaded model.
    """
    model = joblib.load(model_path)

    return model

def save_model(model, model_path: str):
    """
    Save a model to disk.

    Args:
        model: The model to be saved.
        model_path (str): The path to save the model file.
    """
    joblib.dump(model, model_path)
