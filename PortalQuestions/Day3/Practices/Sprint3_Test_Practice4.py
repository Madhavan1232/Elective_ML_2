import pandas as pd
import os , sys
from scipy import stats

before_op = list(map(float , input().split(',')))
after_op = list(map(float , input().split(',')))

t_stats , pval = stats.ttest_rel(before_op , after_op)

if t_stats < 0:
    pval_onetails = pval / 2
else:
    pval_onetails = 1 - (pval / 2)

print(f"Before optimization times: {before_op}")
print(f"After optimization times: {after_op}\n")
print(f"T-statistic (two-tailed): {t_stats:.4f}")
print(f"P-value (two-tailed): {pval:.4f}")
print(f"P-value (one-tailed): {pval_onetails:.4f}")

if pval < 0.05:
    print("Fail to reject null hypothesis: No significant improvement in delivery time.")
else:
    print("Reject null hypothesis: Delivery time improved after optimization.")