import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the wearable device data by cleaning, transforming, and normalizing the data.

    Args:
        data (pd.DataFrame): The raw wearable device data.

    Returns:
        pd.DataFrame: The preprocessed wearable device data.
    """
    # Clean the data by removing missing values and outliers
    data = data.dropna()
    data = data[data < 1000]

    # Transform the data by calculating the mean and standard deviation
    data['mean_hr'] = data['heart_rate'].rolling(window=5).mean()
    data['std_hr'] = data['heart_rate'].rolling(window=5).std()

    # Normalize the data by scaling the heart rate values between 0 and 1
    data['scaled_hr'] = (data['heart_rate'] - data['heart_rate'].min()) / (data['heart_rate'].max() - data['heart_rate'].min())

    return data

def analyze_data(data: pd.DataFrame) -> None:
    """
    Analyze the wearable device data by visualizing the heart rate over time.

    Args:
        data (pd.DataFrame): The preprocessed wearable device data.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['timestamp'], data['heart_rate'], label='Heart Rate')
    plt.plot(data['timestamp'], data['mean_hr'], label='Mean Heart Rate')
    plt.plot(data['timestamp'], data['std_hr'], label='Standard Deviation')
    plt.xlabel('Time')
    plt.ylabel('Heart Rate')
    plt.title('Wearable Device Data Analysis')
    plt.legend()
    plt.show()
