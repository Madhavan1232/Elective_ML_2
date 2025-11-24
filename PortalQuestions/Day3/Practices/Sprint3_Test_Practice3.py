import pandas as pd
import os , sys
from scipy import stats

df = pd.read_csv(os.path.join(sys.path[0] , input()))

east = df[df['Zone'] == 'East']['Delivery_Time_Hours']
west = df[df['Zone'] == 'West']['Delivery_Time_Hours']

t_stats , pval = stats.ttest_ind(east , west , equal_var = True)

print(f"East Mean: {east.mean():.2f}")
print(f"West Mean: {west.mean():.2f}")

print(f"T-statistic: {t_stats:.4f}")
print(f"P-value: {pval:.4f}")

if pval < 0.05:
    print("Reject the null hypothesis: There IS a significant difference in delivery times between East and West.")
else:
    print("Fail to reject the null hypothesis: No significant difference in delivery times between East and West.")