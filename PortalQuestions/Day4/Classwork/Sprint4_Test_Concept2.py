import pandas as pd
import os , sys
from scipy.stats import chi2_contingency

path = os.path.join(sys.path[0] , input())
df = pd.read_csv(path)


contig_table = df[['Electronics Sales' , 'Clothing Sales' , 'Home Goods Sales']].values
print("Contingency Table (Observed Frequencies):")
print(contig_table)

chi2 , p_value , dof , expected = chi2_contingency(contig_table)

print(f"\nChi-square Statistic: {chi2.round(2)}")
print(f"p-value: {p_value}")
print(f"Degrees of Freedom: {dof}")

print("\nExpected Frequencies:")
print(expected)

if p_value < 0.05:
    print("Reject the null hypothesis.")
    print("There is enough evidence to suggest that product sales depend on months (they are related).")
else:
    print("Not reject the hypothesis")