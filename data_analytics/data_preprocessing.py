import pandas as pd
import numpy as np

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input data by removing missing values and outliers.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        pd.DataFrame: The cleaned data.
    """
    # Remove rows with missing values
    data = data.dropna()

    # Remove outliers using the IQR method
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    data = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]

    return data

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms the input data by applying transformations like encoding categorical variables, scaling, and feature engineering.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        pd.DataFrame: The transformed data.
    """
    # Encode categorical variables
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column] = data[column].astype('category').cat.codes

    # Scale numeric variables
    for column in data.columns:
        if data[column].dtype == 'float64' or data[column].dtype == 'int64':
            data[column] = (data[column] - data[column].mean()) / data[column].std()

    # Perform feature engineering
    # ...

    return data
