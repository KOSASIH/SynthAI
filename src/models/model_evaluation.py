from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the performance of the input model on the test data.

    Args:
        model: The input model to be evaluated.
        X_test (pd.DataFrame): The test data features.
        y_test (pd.Series): The test data target.

    Returns:
        float: The mean squared error of the model on the test data.
    """
    # make predictions on the test data
    y_pred = model.predict(X_test)

    # calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)

    return mse
