import pandas as pd
import os , sys
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(os.path.join(sys.path[0] , input()))

data_df = df[['Customer_Age' , 'Order_Quantity' , 'Unit_Cost' , 'Unit_Price' , 'Revenue']]
print("First 5 rows of selected data:")
print(data_df.head())

print("\nMissing values before treatment:")
null_counts = data_df.isnull().sum()
print(null_counts)

data_df = data_df.fillna(data_df.mean())
after_null_counts = data_df.isnull().sum()
print("\nMissing values after treatment:")
print(after_null_counts)

for col in data_df.columns:
    q1 = data_df[col].quantile(0.25)
    q3 = data_df[col].quantile(0.75)
    
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    
    data_df[col] = data_df[col].clip(lower = lower , upper = upper).astype(float)

print("\nOutlier treatment done. DataFrame with capped outliers:")
print(data_df.head())


print("\nFirst 5 rows after scaling:")
scalar = StandardScaler()
scalar_data = scalar.fit_transform(data_df)
res_scalar = pd.DataFrame(scalar_data , columns = data_df.columns , index = data_df.index)
print(res_scalar.head())

print("Correlation of features with Revenue (sorted):")
cor = data_df.corr()[['Revenue']].sort_values()
cor_df = pd.DataFrame(cor , columns = ['Revenue'])
print(cor_df)
