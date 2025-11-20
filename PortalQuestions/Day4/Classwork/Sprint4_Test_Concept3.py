import pandas as pd
import os, sys
from scipy.stats import chi2_contingency

path = os.path.join(sys.path[0] , input())
df = pd.read_csv(path)

table = ['Electronics' , 'Clothing' , 'Home Goods']

table_df = df[table].copy()
table_df.index = ['Q1' , 'Q2' , 'Q3' , 'Q4']
chi , p_value , dof , expected = chi2_contingency(table_df)

print("Contingency Table (Observed Frequencies):")
print(table_df.values)
print(f"\nChi-Square Statistic: {chi.round(2)}")
print(f"Degrees of Freedom: {dof}")
print(f"P-Value: {p_value.round(2)}\n")
res = pd.DataFrame(expected , index = table_df.index , columns = table_df.columns)
print("Expected Frequencies:")
print(res)

if p_value < 0.05:
    print("Reject the null hypothesis.")
    print("There is enough evidence to suggest that the distribution of sales is different across the four quarters.")
else:
    print("Do not reject the null hypothesis.")    
    print("There is not enough evidence to suggest that the distribution of sales is different across the four quarters.")