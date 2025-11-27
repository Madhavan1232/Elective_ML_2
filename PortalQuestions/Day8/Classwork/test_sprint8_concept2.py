import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
import os
import sys

# Read the CSV file
filename = input().strip()
df = pd.read_csv(os.path.join(sys.path[0], filename))

# Display shape of dataset
print(f"Shape of dataset: {df.shape}")

# Prepare features and target
X = df.drop('not.fully.paid', axis=1)
y = df['not.fully.paid']

# Split into train and test sets (80:20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display sizes
print(f"Size of training dataset: {X_train.shape}")
print(f"Size of test dataset: {X_test.shape}")

# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Extract TN, FP, FN, TP (assuming binary classification)
if cm.shape == (2, 2):
    tn, fp, fn, tp = cm.ravel()
else:
    # Handle case where one class is missing
    if cm.shape == (1, 1):
        if y_test.iloc[0] == 0:
            tn = cm[0][0]
            fp = fn = tp = 0
        else:
            tp = cm[0][0]
            tn = fp = fn = 0
    else:
        tn = fp = fn = tp = 0  # Fallback

# Evaluation Metrics
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, zero_division=0)
precision = precision_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\nEvaluation Metrics:")
print(f"Accuracy : {accuracy}")
print(f"Recall   : {recall}")
print(f"Precision: {precision}")
print(f"F1-score : {f1}")
