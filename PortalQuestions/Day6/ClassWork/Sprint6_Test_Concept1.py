import pandas as pd
import os , sys
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  mean_squared_error , mean_absolute_error , r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv(os.path.join(sys.path[0] , input()))
print("First 5 rows of dataset:")
print(df.head())

print("Available Columns:")
print(list(df.columns))

x = df[['global_radiation']]
y = df['temperature']

x_train , x_test , y_train , y_test = train_test_split(
    x , y , test_size = 0.3 , random_state = 200)

model = LinearRegression()
model.fit(x_train , y_train)

y_pred = model.predict(x_train)

intercept = model.intercept_
score = r2_score(y_train , y_pred)
slope = model.coef_
print("\nModel Trained")
print(f"R² Score (Train): {score:.4f}")
print(f"Intercept       : {intercept:.4f}")
print(f"Slope           : {slope[0]:.4f}")

y_pred_test = model.predict(x_test)
print("\nEvaluation Metrics:")
mean = mean_squared_error(y_test , y_pred_test)
mean_abo = mean_absolute_error(y_test , y_pred_test)
root = np.sqrt(mean)
r2score = r2_score(y_test , y_pred_test)

print(f"Mean Squared Error (MSE) : {mean:.4f}")
print(f"Mean Absolute Error (MAE): {mean_abo:.4f}")
print(f"Root Mean Squared Error  : {root:.4f}")
print(f"R² Score (Test)          : {r2score:.4f}")
