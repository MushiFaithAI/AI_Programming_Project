import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv(os.path.join("data","dataset.csv"))

# Clean column names
data.columns = data.columns.str.strip()

# Convert target (Yes/No → 1/0)
data['Purchased'] = data['Purchased'].str.strip().str.lower().map({'yes':1,'no':0})

# Features and target
X = data[['Age','Salary','Discount']]
y = data['Purchased']

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, pred)

print("Predictions:", pred)
print("Accuracy:", acc)