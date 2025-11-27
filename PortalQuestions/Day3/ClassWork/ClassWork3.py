import sys
import numpy as np
from scipy import stats

def main():
    try:
        mean_male = float(sys.stdin.readline().strip())
        sd_male = float(sys.stdin.readline().strip())
        n_male = int(sys.stdin.readline().strip())
        mean_female = float(sys.stdin.readline().strip())
        sd_female = float(sys.stdin.readline().strip())
        n_female = int(sys.stdin.readline().strip())
    except Exception as e:
        print("Error reading inputs:", e)
        return

    np.random.seed(42)
    male_samples = np.random.normal(loc=mean_male, scale=sd_male, size=n_male)
    female_samples = np.random.normal(loc=mean_female, scale=sd_female, size=n_female)

    t_stat, p_value = stats.ttest_ind(male_samples, female_samples, equal_var=True)

    alpha = 0.05

    # Print results
    print("Two-Sample T-Test Result (Male vs Female Fit Ratings)")
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")

    if p_value < alpha:
        print("Reject the null hypothesis: Significant difference in fit ratings between male and female respondents.")
    else:
        print("Fail to reject the null hypothesis: No significant difference in fit ratings between male and female respondents.")

if __name__ == "__main__":
    main()