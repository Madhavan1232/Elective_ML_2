import pandas as pd
import os , sys
from scipy.stats import norm
import numpy as np


df = pd.read_csv(os.path.join(sys.path[0] , input()))

north = df[df['Zone'] == 'North']['Delivery_Time_Hours']
south = df[df['Zone'] == 'South']['Delivery_Time_Hours']

n = min(len(north) , (len(south)))

north_sample = north.sample(n = n , random_state = 42)
south_sample = south.sample(n = n , random_state = 42)

print(f"Sample Size per Group: {n}")
print(f"Mean Delivery Time (North): {north_sample.mean():.2f}")
print(f"Mean Delivery Time (South): {south_sample.mean():.2f}")

zstats = (north_sample.mean() - south_sample.mean()) / (1.41 * np.sqrt(2 / n))
pval = 2 * norm.sf(abs(zstats))

print(f"Z-Statistic: {zstats:.4f}")
print(f"P-Value: {pval:.4f}")

if pval < 0.05:
    print("Reject the null hypothesis: There IS a significant difference in delivery times.")
else:
    print("Fail to reject the null hypothesis: No significant difference in delivery times.")