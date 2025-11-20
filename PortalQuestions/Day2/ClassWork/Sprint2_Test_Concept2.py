import pandas as pd
import os , sys
import numpy as np
from scipy import stats

file = input()
path = os.path.join(sys.path[0] , file)
df = pd.read_csv(path)
print(f"File loaded successfully: {file}")
print(f"Data shape: {df.shape}")
print("Preview of Loaded Data:")
print(df.head())


np.random.seed(42)
sample_df = df.sample(n = 50)
sample_df = sample_df.reset_index(drop = True)

print("Simple Random Sampling (50 students):")
print(sample_df.head())

print("Summary Statistics of the Population data")
print(df['Height_cm'].describe().round(1))

print(f"median: {df['Height_cm'].median()} mode: {df['Height_cm'].mode()[0]}")

print(f"skewness: {stats.skew(df['Height_cm']):.3f} kurtosis: {stats.kurtosis(df['Height_cm']):.3f}")


print("Summary Statistics of the Sample data") 
print(sample_df['Height_cm'].describe().round(1)) 

print(f"median: {sample_df['Height_cm'].median()} mode: {sample_df['Height_cm'].mode()[0]}") 

print(f"skewness: {stats.skew(sample_df['Height_cm']):.3f} kurtosis: {stats.kurtosis(sample_df['Height_cm']):.3f}")
