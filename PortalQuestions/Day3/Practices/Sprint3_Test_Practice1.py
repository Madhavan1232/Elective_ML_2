import pandas as pd
import os, sys
import numpy as np
from scipy.stats import norm

file = input()
df = pd.read_csv(os.path.join(sys.path[0] , file))

mu_0 = float(input())
sigma = float(input())

mean = df['Delivery_Time_Hours'].mean()
n = len(df['Delivery_Time_Hours'])
zstats = (mean - mu_0) / (sigma / np.sqrt(n))
pval = 2 * norm.sf(abs(zstats))


print(f"File loaded successfully: {file}")
print(f"Data shape: {df.shape}\n")
print(f"Z-statistic: {zstats:.4f}")
print(f"P-value: {pval:.4f}")

if pval < 0.05:
    print("Reject the null hypothesis. There is enough evidence to suggest the delivery time differs from the hypothesized mean.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to suggest the delivery time differs from the hypothesized mean.")