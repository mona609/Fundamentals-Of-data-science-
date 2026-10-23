import numpy as np

student_scores = np.array([
    [80, 75, 85, 70],
    [90, 85, 80, 75],
    [70, 80, 75, 85],
    [85, 90, 88, 80]
])

subjects = ["Math", "Science", "English", "History"]

average_scores = np.mean(student_scores, axis=0)

print("Average score for each subject:")
for i in range(4):
    print(subjects[i], ":", average_scores[i])

highest_subject = subjects[np.argmax(average_scores)]

print("Subject with highest average score:", highest_subject)
