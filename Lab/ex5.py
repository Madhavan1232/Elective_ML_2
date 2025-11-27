import pandas as pd
from scipy.stats import chisquare, chi2_contingency
import os ,sys
file = input().strip()
filepath = os.path.join(sys.path[0],file)

df = pd.read_csv(filepath)

df = df.dropna()

exp_adelie = int(input())
exp_chinstrap = int(input())
exp_gentoo = int(input())

expected_raw = [exp_adelie, exp_chinstrap, exp_gentoo]


observed = df["species"].value_counts().reindex(["Adelie", "Chinstrap", "Gentoo"])

expected = pd.Series(expected_raw)
expected = expected / expected.sum() * observed.sum()

chi_stat_gof, p_value_gof = chisquare(f_obs=observed, f_exp=expected)

print("Chi-Square Goodness of Fit:")
print("Chi-Square Statistic:", chi_stat_gof)
print("p-Value:", p_value_gof)
print("Conclusion:", "Reject H0" if p_value_gof < 0.05 else "Fail to Reject H0")
print()

contingency_table = pd.crosstab(df["species"], df["island"])

chi_stat_ind, p_value_ind, dof, expected_table = chi2_contingency(contingency_table)

print("Chi-Square Test of Independence:")
print("Chi-Square Statistic:", chi_stat_ind)
print("p-Value:", p_value_ind)
print("Conclusion:", "Reject H0" if p_value_ind < 0.05 else "Fail to Reject H0")
print()
