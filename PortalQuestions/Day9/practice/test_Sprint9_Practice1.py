import numpy as np
import pandas as pd
import os , sys
from sklearn.model_selection import train_test_split

df = pd.read_csv(os.path.join(sys.path[0] , input()))

print(f"Dataset Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

print("\nTarget class distribution:")
print(df['Outcome'].value_counts())

print("\nData Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

Input_df = df.drop(columns = 'Outcome')
output_df = df['Outcome']

print(f"\nInputs Shape: {Input_df.shape}")
print(f"Outputs Shape: {output_df.shape}")

train_df , test_df = train_test_split(Input_df , test_size = 0.2 , random_state = 42)
print(f"\nTraining set size: {train_df.shape}")
print(f"Testing set size: {test_df.shape}")