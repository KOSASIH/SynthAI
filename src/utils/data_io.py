import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.
    """
    data = pd.read_csv(file_path)

    return data

def save_data(data: pd.DataFrame, file_path: str):
    """
    Save data to a CSV file.

    Args:
        data (pd.DataFrame): The data to be saved.
        file_path (str): The path to save the CSV file.
    """
    data.to_csv(file_path, index=False)
