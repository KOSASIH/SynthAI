import pandas as pd

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the input data by removing any missing or invalid values.

    Args:
        data (pd.DataFrame): The input data to be cleaned.

    Returns:
        pd.DataFrame: The cleaned data.
    """
    # remove any rows with missing values
    data.dropna(inplace=True)

    # remove any rows with invalid values
    data = data[data['column_name'].apply(lambda x: is_valid_value(x))]

    return data

def is_valid_value(value):
    # custom validation logic
    ...
