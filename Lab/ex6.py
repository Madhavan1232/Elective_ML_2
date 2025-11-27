import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import os, sys
import numpy as np
file_name = input().strip()
df = pd.read_csv(os.path.join(sys.path[0], file_name))

print("Missing Data:")
print(df.isnull().sum())
print()

df_dropna = df.dropna()
print("Dataset after dropping missing values:")
print(df_dropna)
print()

numeric_cols = df.select_dtypes(include=np.number).columns
mean_imputer = SimpleImputer(strategy='mean')
median_imputer = SimpleImputer(strategy='median')

df_mean_filled = df.copy()
df_median_filled = df.copy()

df_mean_filled[numeric_cols] = mean_imputer.fit_transform(df_mean_filled[numeric_cols])
df_median_filled[numeric_cols] = median_imputer.fit_transform(df_median_filled[numeric_cols])

scaler_standard = StandardScaler()
scaler_minmax = MinMaxScaler()

loan_amount_values = df_mean_filled[['LoanAmount']].dropna()

standardized = scaler_standard.fit_transform(loan_amount_values)
normalized = scaler_minmax.fit_transform(loan_amount_values)

df_standardized_loan_amount = pd.DataFrame(standardized, columns=['LoanAmount_Standardized'])
df_normalized_loan_amount = pd.DataFrame(normalized, columns=['LoanAmount_Normalized'])

print("Standardized LoanAmount:")
print(df_standardized_loan_amount)
print()

print("Normalized LoanAmount:")
print(df_normalized_loan_amount)
