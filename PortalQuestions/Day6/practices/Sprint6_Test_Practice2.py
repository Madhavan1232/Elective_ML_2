import pandas as pd
import numpy as np
import os, sys
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression


data = pd.read_csv(os.path.join(sys.path[0], input()))
df = data[["Customer_Age", "Order_Quantity", "Unit_Cost", "Unit_Price", "Revenue"]]

df = df.fillna(df.mean())

for col in df.columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    
    df[col] = df[col].clip(lower=lower, upper=upper).astype(float)

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

x = df_scaled[["Unit_Cost"]]
y = df_scaled["Revenue"]

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=200)

model = LinearRegression()
model.fit(xtrain, ytrain)

intercept = model.intercept_
slope = model.coef_[0]

print(f"Intercept: {intercept}")
print(f"Slope: {slope}")