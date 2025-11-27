import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, norm
import os , sys

dataset_path = input().strip()
mu0_sales = int(input().strip())
mu0_tv = int(input().strip())

df = pd.read_csv(os.path.join(sys.path[0] , dataset_path))

sales = df['Sales']
tv = df['TV']

sample_mean_sales = sales.mean()
sample_std_sales = sales.std()
n_sales = len(sales)
z_stat_one = (sample_mean_sales - mu0_sales) / (sample_std_sales / np.sqrt(n_sales))
p_value_one = 2 * (1 - norm.cdf(abs(z_stat_one)))
conclusion_one = "Reject H0" if p_value_one < 0.05 else "Fail to Reject H0"

print("One-Sample Z-Test (Sales):")
print(f"Z-Statistic: {z_stat_one}")
print(f"p-Value: {p_value_one}")
print(f"Conclusion: {conclusion_one}")

sales_a = sales[:100]
sales_b = sales[100:200]
mean_a = sales_a.mean()
mean_b = sales_b.mean()
std_a = sales_a.std()
std_b = sales_b.std()
n_a = 100
n_b = 100
z_stat_two = (mean_a - mean_b) / np.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
p_value_two = 2 * (1 - norm.cdf(abs(z_stat_two)))
conclusion_two = "Reject H0" if p_value_two < 0.05 else "Fail to Reject H0"

print("\nTwo-Sample Z-Test (Sales Groups):")
print(f"Z-Statistic: {z_stat_two}")
print(f"p-Value: {p_value_two}")
print(f"Conclusion: {conclusion_two}")

t_stat_tv_one, p_value_tv_one = ttest_1samp(tv, mu0_tv)
conclusion_tv_one = "Reject H0" if p_value_tv_one < 0.05 else "Fail to Reject H0"

print("\nOne-Sample T-Test (TV):")
print(f"T-Statistic: {t_stat_tv_one}")
print(f"p-Value: {p_value_tv_one}")
print(f"Conclusion: {conclusion_tv_one}")

tv_a = tv[:100]
tv_b = tv[100:200]
t_stat_tv_two, p_value_tv_two = ttest_ind(tv_a, tv_b)
conclusion_tv_two = "Reject H0" if p_value_tv_two < 0.05 else "Fail to Reject H0"

print("\nTwo-Sample T-Test (TV Groups):")
print(f"T-Statistic: {t_stat_tv_two}")
print(f"p-Value: {p_value_tv_two}")
print(f"Conclusion: {conclusion_tv_two}")