import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def descriptive_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """
    Computes descriptive statistics for the input data.

    Args:
        data (pd.DataFrame): The input data.

    Returns:
        pd.DataFrame: The dataframe containing the descriptive statistics.
    """
    statistics = data.describe()

    return statistics

def data_visualization(data: pd.DataFrame) -> None:
    """
    Visualizes the input data using plots.

    Args:
        data (pd.DataFrame): The input data.
    """
    # Histograms for each variable
    for column in data.columns:
        sns.histplot(data=data, x=column)
        plt.show()

    # Correlation matrix
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.show()

    # Pairplot
    sns.pairplot(data)
    plt.show()
