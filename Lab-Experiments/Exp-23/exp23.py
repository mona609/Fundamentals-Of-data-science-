import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Improvement in symptom score after the trial (higher = better)
control = np.array([4.7, 3.1, 1.1, 5.4, 4.8, 0.4, 2.1, 0.2, -0.3, 7.4, 2.1, 4.7, 3.8, 3.2, 0.4, 0.5, 4.1, 5.8, -1.6, 0.7, 2.5, 5.6, 4.3, 5.0, 3.6, 0.6, 2.7, 6.2, 3.4, -0.1])      # placebo group
treatment = np.array([10.5, 8.1, 8.8, 11.9, 5.6, 5.3, 0.7, 7.4, 8.5, 6.9, 7.0, 9.3, 8.1, 8.0, 6.8, 6.9, 9.6, 6.8, 5.9, 5.6, 6.7, 7.5, 8.3, 7.3, 6.2, 2.9, 8.5, 4.5, 6.6, 10.0])  # new drug group

# Hypotheses
# H0: mean improvement is the same in both groups
# H1: mean improvement is different

# Independent two-sample t-test
t_stat, p_value = stats.ttest_ind(treatment, control)
alpha = 0.05
df = len(control) + len(treatment) - 2

print(f"Mean improvement (placebo)  : {control.mean():.2f}")
print(f"Mean improvement (treatment): {treatment.mean():.2f}")
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value     = {p_value:.2e}")

if p_value < alpha:
    print("p-value < 0.05, so reject H0. The treatment has a significant effect.")
else:
    print("p-value >= 0.05, so do not reject H0. No significant effect found.")

# ---------- Visualisation ----------
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

# Left: box plot of the two groups
axes[0].boxplot([control, treatment])
axes[0].set_xticks([1, 2])
axes[0].set_xticklabels(["Placebo", "Treatment"])
axes[0].set_ylabel("Improvement in symptom score")
axes[0].set_title("Placebo vs Treatment")

# Right: t-distribution with the p-value area shaded
limit = max(6, abs(t_stat) + 1)
x = np.linspace(-limit, limit, 500)
y = stats.t.pdf(x, df)
axes[1].plot(x, y, color="black")
axes[1].fill_between(x, y, where=(x <= -abs(t_stat)), color="red", alpha=0.5)
axes[1].fill_between(x, y, where=(x >= abs(t_stat)), color="red", alpha=0.5)
t_crit = stats.t.ppf(1 - alpha / 2, df)
axes[1].axvline(-t_crit, color="blue", linestyle="--", label="critical values (5%)")
axes[1].axvline(t_crit, color="blue", linestyle="--")
axes[1].axvline(t_stat, color="red", label=f"t = {t_stat:.2f}")
axes[1].set_title(f"t-distribution, p-value = {p_value:.2e}")
axes[1].set_xlabel("t value")
axes[1].legend()

plt.tight_layout()
plt.show()
