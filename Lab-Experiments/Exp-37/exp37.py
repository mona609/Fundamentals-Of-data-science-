import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Study time (hours) and exam score of 20 students
study_hours = np.array([1, 1.5, 2, 2, 2.5, 3, 3, 3.5, 4, 4, 4.5, 5, 5.5, 6, 6, 6.5, 7, 7.5, 8, 9])
exam_scores = np.array([38, 45, 46, 37, 57, 57, 52, 51, 63, 52, 63, 70, 69, 69, 69, 73, 84, 90, 84, 89])

# ---------- Correlation ----------
pearson_r, pearson_p = stats.pearsonr(study_hours, exam_scores)
spearman_r, spearman_p = stats.spearmanr(study_hours, exam_scores)

print(f"Pearson correlation  : {pearson_r:.3f} (p = {pearson_p:.2e})")
print(f"Spearman correlation : {spearman_r:.3f} (p = {spearman_p:.2e})")

if pearson_r > 0.7:
    print("Strong positive correlation: more study time gives higher scores.")
elif pearson_r > 0.3:
    print("Moderate positive correlation.")
else:
    print("Weak or no correlation.")

# Line of best fit
slope, intercept = np.polyfit(study_hours, exam_scores, 1)
print(f"\nBest fit line: score = {slope:.2f} x hours + {intercept:.2f}")

# ---------- Visualisation using different plots ----------
fig, axes = plt.subplots(2, 2, figsize=(11, 8))

# 1. Scatter plot with the trend line
axes[0, 0].scatter(study_hours, exam_scores, color="blue")
axes[0, 0].plot(study_hours, slope * study_hours + intercept, color="red")
axes[0, 0].set_title("Scatter plot with trend line")
axes[0, 0].set_xlabel("Study hours")
axes[0, 0].set_ylabel("Exam score")

# 2. Line plot of the scores in order of study time
axes[0, 1].plot(study_hours, exam_scores, marker="o", color="green")
axes[0, 1].set_title("Line plot")
axes[0, 1].set_xlabel("Study hours")
axes[0, 1].set_ylabel("Exam score")

# 3. Bar chart of the average score for each study-time group
data = pd.DataFrame({"hours": study_hours, "score": exam_scores})
data["group"] = pd.cut(data["hours"], bins=[0, 3, 6, 10], labels=["0-3 h", "3-6 h", "6-10 h"])
group_mean = data.groupby("group", observed=True)["score"].mean()
axes[1, 0].bar(group_mean.index.astype(str), group_mean.values, color="orange")
axes[1, 0].set_title("Average score by study time")
axes[1, 0].set_xlabel("Study time group")
axes[1, 0].set_ylabel("Average score")

# 4. Heatmap of the correlation matrix
corr = data[["hours", "score"]].corr()
image = axes[1, 1].imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
axes[1, 1].set_xticks([0, 1])
axes[1, 1].set_xticklabels(["hours", "score"])
axes[1, 1].set_yticks([0, 1])
axes[1, 1].set_yticklabels(["hours", "score"])
for i in range(2):
    for j in range(2):
        axes[1, 1].text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
axes[1, 1].set_title("Correlation heatmap")
fig.colorbar(image, ax=axes[1, 1])

plt.tight_layout()
plt.show()
