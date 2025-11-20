import math
from scipy.stats import norm
from statsmodels.stats.weightstats import ztest

x = float(input())
hy_mean = float(input())
pop_std = float(input())
size = int(input())
typ = input().strip().lower()

alpha_level = input()
alpha = float(alpha_level) if alpha_level else 0.05

z_stat = (x - hy_mean) /( pop_std / (math.sqrt(size)))

if typ == "greater":
    p_val = 1 - norm.cdf(z_stat)
elif typ == "less":
    p_val = norm.cdf(z_stat)
else:
    p_val = 2 * (1 - norm.cdf(abs(z_stat)))

print(f"Z-statistic: {round(z_stat , 4)}")
print(f"P-value: {round(p_val , 4)}")

if p_val < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
    