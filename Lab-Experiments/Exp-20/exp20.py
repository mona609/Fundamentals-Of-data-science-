import numpy as np
from scipy import stats

# Daily conversion rate (%) for 14 days
design_a = np.array([2.1, 2.4, 2.0, 2.6, 2.3, 2.2, 2.5, 2.1, 2.4, 2.3, 2.2, 2.6, 2.0, 2.5])
design_b = np.array([2.9, 3.1, 2.8, 3.3, 3.0, 2.7, 3.2, 3.0, 2.9, 3.4, 2.8, 3.1, 3.0, 3.2])

print(f"Mean conversion rate of design A: {design_a.mean():.3f}%")
print(f"Mean conversion rate of design B: {design_b.mean():.3f}%")

# Independent two-sample t-test (Welch's t-test)
t_stat, p_value = stats.ttest_ind(design_a, design_b, equal_var=False)

alpha = 0.05
print(f"\nt-statistic = {t_stat:.4f}")
print(f"p-value     = {p_value:.2e}")

if p_value < alpha:
    print("Result: p-value < 0.05, so reject H0. There IS a significant difference between design A and design B.")
else:
    print("Result: p-value >= 0.05, so do not reject H0. There is NO significant difference between the designs.")
