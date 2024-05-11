import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load data from blockchain-based ledger
data = pd.read_csv('ledger_data.csv')

# Preprocess data
X = data.drop(['target'], axis=1)
y = data['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train random forest classifier
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X_train, y_train)

# Evaluate model performance
accuracy = rfc.score(X_test, y_test)
print(f'Model accuracy: {accuracy:.3f}')
