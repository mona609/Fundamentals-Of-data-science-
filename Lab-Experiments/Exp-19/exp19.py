import numpy as np
from scipy import stats

# Reduction in blood pressure (mmHg) of 25 patients in each group
drug = np.array([23.5, 12.7, 15.2, 17.0, 11.1, 15.0, 15.0, 6.2, 20.1, 18.0, 11.9, 14.1, 17.5, 13.7, 13.8, 7.7, 17.8, 15.6, 16.4, 7.4, 23.3, 15.8, 13.1, 25.1, 14.8])
placebo = np.array([-0.8, 3.4, -4.2, 9.2, 3.3, 2.0, 9.3, -1.6, 7.1, -3.3, 2.4, 0.2, 10.8, 12.1, 3.7, 8.4, 4.3, 7.3, 2.0, -1.8, -2.2, 6.5, 14.0, 6.1, 2.9])


def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    sem = stats.sem(data)                      # standard error of the mean
    low, high = stats.t.interval(confidence, df=n - 1, loc=mean, scale=sem)
    return mean, low, high


for name, group in [("Drug", drug), ("Placebo", placebo)]:
    mean, low, high = confidence_interval(group)
    print(f"{name} group: mean reduction = {mean:.2f} mmHg")
    print(f"  95% confidence interval = ({low:.2f}, {high:.2f})\n")
