import numpy as np
from statsmodels.stats.weightstats import ztest

boy_hei = float(input())
std_boy = float(input())
n_boys = int(input())

girl_hei = float(input())
std_girl = float(input())
n_girls = int(input())

np.random.seed(42)

boys_hei = np.random.normal(loc = boy_hei , scale = std_boy , size = n_boys)
girls_hei = np.random.normal(loc = girl_hei ,scale = std_girl , size = n_girls)

print("Two-Sample Z-Test Result (Boys > Girls)")

z_stats , p_value = ztest(boys_hei , girls_hei , alternative = "larger")

print(f"Z-statistic: {z_stats:.4f}")
print(f"P-value: {p_value:.4f}")


if p_value < 0.05:
    print("Reject the null hypothesis: Boys are significantly taller than girls.")
else:
    print("Fail to reject the null hypothesis: No significant evidence that boys are taller than girls.")