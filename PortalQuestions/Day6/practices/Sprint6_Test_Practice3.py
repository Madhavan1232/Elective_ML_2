import pandas as pd
import numpy as np
import os , sys
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


data_df = pd.read_csv(os.path.join(sys.path[0] , input()))

df = data_df[['Customer_Age' , 'Order_Quantity' , 'Unit_Cost' , 'Unit_Price' , 'Revenue']]
df = df.fillna(df.mean())

for col in df.columns:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    
    df[col] = df[col].clip(lower = lower , upper = upper).astype(float)

scalar = StandardScaler() 
df_scaled = pd.DataFrame(scalar.fit_transform(df) , columns = df.columns)

x = df_scaled[['Unit_Cost']]
y = df_scaled['Revenue']

x_train , x_test , y_train , y_test = train_test_split(x , y , test_size = 0.3 , random_state = 200)

model = LinearRegression()
model.fit(x_train , y_train)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test , y_pred)
mae = mean_absolute_error(y_test , y_pred)
root = np.sqrt(mse)
score = r2_score(y_test , y_pred)


print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {root:.4f}", )
print(f"R2 Score: {score:.4f}")
