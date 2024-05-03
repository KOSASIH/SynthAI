import joblib

def deploy_model(model, model_path: str):
    """
    Deploy the input model by saving it to disk.

    Args:
        model: The input model to be deployed.
        model_path (str): The path to save the model.
    """
    # save the model to disk
    joblib.dump(model, model_path)
