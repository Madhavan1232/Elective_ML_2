import pandas as pd
import os , sys

df = pd.read_csv(os.path.join(sys.path[0] , input()))

print("Loan Data Analysis Started.\n")

print("First 5 Rows")
print(df.head())

print("Column Names")
print(list(df.columns))

print("Dataset Shape")
rows , cols = df.shape
print(f"Rows: {rows}, Columns: {cols}")

print("Column Data Types and Non-Null Counts")
for col in df.columns:
    not_null = df[col].notnull().sum()
    Dtype = df[col].dtype
    print(f"{col:22} Non-Null: {not_null} Type: {Dtype}")

print("Summary Statistics")
print(df.describe())

print("Value Counts for 'purpose'")
print(df['purpose'].value_counts())

print("Value Counts for 'credit.policy'")
print(df['credit.policy'].value_counts())

print("Value Counts for 'not.fully.paid'")
print(df['not.fully.paid'].value_counts())







