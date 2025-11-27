import os
import pandas as pd
from sklearn.linear_model import LinearRegression

file_name = input().strip()

current_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_directory, file_name)

df = pd.read_csv(file_path)

model = LinearRegression()
model.fit(df[["x"]] , df["y"])

y_pred = model.predict([[10]])[0]
print(f"Intercept: {model.intercept_:.4f}")
print(f"Estimated value at x=10: {y_pred:.4f}")