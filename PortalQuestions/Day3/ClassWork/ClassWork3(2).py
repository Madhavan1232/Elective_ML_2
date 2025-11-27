import numpy as np
from scipy.stats import ttest_rel

np.random.seed(42)

mean_before = float(input())
sd_before = float(input())
mean_after = float(input())
sd_after = float(input())
n = int(input())

mean_diff = mean_after - mean_before
sd_diff = abs(sd_before - sd_after)

before = np.random.normal(mean_before, sd_before, n)
noise = np.random.normal(0, sd_diff, n)
after = before + mean_diff + noise

t_stat, p_val = ttest_rel(before, after)

t_stat = abs(t_stat)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}")
if p_val < 0.05:
    print("Reject the null hypothesis. There is a significant difference in fit ratings before and after the intervention.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference in fit ratings before and after the intervention.")