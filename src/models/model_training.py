import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(data: pd.DataFrame, target_column: str) -> LinearRegression:
    """
    Train a linear regression model on the input data.

    Args:
        data (pd.DataFrame): The input data to be used for training.
        target_column (str): The name of the target column.

    Returns:
        LinearRegression: The trained linear regression model.
    """
    # split the data into features and target
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # train the model
    model = LinearRegression()
    model.fit(X, y)

    return model
