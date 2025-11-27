import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import numpy as np
import os ,sys

def evaluate_classifier(model, X_train, X_test, y_train, y_test, model_name, target_names):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro', zero_division=0)
    recall = recall_score(y_test, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=0)
    cm = confusion_matrix(y_test, y_pred)
    cr = classification_report(y_test, y_pred, target_names=target_names, digits=3, zero_division=0)

    print(f"{model_name}")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision (macro): {precision:.2f}")
    print(f"Recall (macro): {recall:.2f}")
    print(f"F1-score (macro): {f1:.2f}")
    print("Confusion Matrix:")
    print(cm)
    print("Classification Report:")
    print(cr)

def main():
    file_name = input()

    df = pd.read_csv(os.path.join(sys.path[0] , file_name))


    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['species']

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    target_names = ['setosa', 'versicolor', 'virginica']

    original_target_names = le.inverse_transform(np.arange(len(le.classes_)))

    encoded_to_display_name = {le.transform([name])[0]: name for name in target_names}

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
    )

    knn = KNeighborsClassifier()
    evaluate_classifier(knn, X_train, X_test, y_train, y_test, "KNN", target_names)

    print() 
    logistic_regression = LogisticRegression(max_iter=1000, random_state=42)
    evaluate_classifier(logistic_regression, X_train, X_test, y_train, y_test, "Logistic Regression", target_names)

if __name__ == "__main__":
    main()
