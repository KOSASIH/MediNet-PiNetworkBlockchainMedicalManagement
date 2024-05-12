from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd

def train_model(data: pd.DataFrame, target: str) -> LogisticRegression:
    """
    Trains a logistic regression model on the input data.

    Args:
        data (pd.DataFrame): The input data.
        target (str): The target variable.

    Returns:
        LogisticRegression: The trained logistic regression model.

    Raises:
        ValueError: If the target variable is not found in the data.
    """
    if target not in data.columns:
        raise ValueError(f"Target variable '{target}' not found in data")

    X = data.drop(columns=[target])
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    return model

def evaluate_model(model: LogisticRegression, X_test: pd.DataFrame, y_test: pd.Series) -> None:
    """
    Evaluates the performance of a logistic regression model.

    Args:
        model (LogisticRegression): The trained logistic regression model.
        X_test (pd.DataFrame): The test data.
        y_test (pd.Series): The true target values.

    Returns:
        None

    Prints:
        Accuracy, Confusion Matrix, and Classification Report of the model.
    """
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)

    print(f"Accuracy: {accuracy:.3f}")
    print(f"Confusion Matrix:\n{conf_matrix}")
    print(f"Classification Report:\n{class_report}")
