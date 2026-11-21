import numpy as np
from scipy import stats

# Read the measurements (one concentration per row, first row is the header)
data = np.genfromtxt("rare_elements.csv", delimiter=",", skip_header=1)
print("Total measurements in the file:", len(data))

# Inputs from the user
n = int(input("Enter the sample size: "))
confidence = float(input("Enter the confidence level in % (e.g. 95): ")) / 100
precision = float(input("Enter the desired precision (margin of error): "))

# Random sample (seed makes the result repeatable)
np.random.seed(42)
sample = np.random.choice(data, size=n, replace=False)

# Point estimate of the population mean
mean = np.mean(sample)
std = np.std(sample, ddof=1)          # sample standard deviation
sem = std / np.sqrt(n)                # standard error of the mean

# Confidence interval using the t-distribution
t_critical = stats.t.ppf((1 + confidence) / 2, df=n - 1)
margin = t_critical * sem
lower = mean - margin
upper = mean + margin

print(f"\nPoint estimate (sample mean) : {mean:.3f}")
print(f"Sample standard deviation    : {std:.3f}")
print(f"Standard error               : {sem:.3f}")
print(f"Margin of error              : {margin:.3f}")
print(f"{confidence * 100:.0f}% confidence interval      : ({lower:.3f}, {upper:.3f})")

# Check the desired precision
if margin <= precision:
    print(f"\nThe margin of error is within the desired precision of {precision}.")
else:
    z = stats.norm.ppf((1 + confidence) / 2)
    required_n = int(np.ceil((z * std / precision) ** 2))
    print(f"\nThe margin of error is larger than the desired precision of {precision}.")
    print(f"A sample size of about {required_n} is needed to reach this precision.")
