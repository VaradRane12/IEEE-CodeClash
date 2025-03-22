import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

data = pd.read_csv("data/sensor_data.csv")

feature_columns = ["object_distance", "velocity", "trajectory_angle", "vehicle_speed"]
X = data[feature_columns]
y = data["collision_risk"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

os.makedirs("models", exist_ok=True)
model_path = os.path.join("models", "risk_assessment_model.pkl")
joblib.dump(model, model_path)

print(f"Model trained with accuracy: {accuracy:.2f}")
print(f"Model saved to '{model_path}'")
