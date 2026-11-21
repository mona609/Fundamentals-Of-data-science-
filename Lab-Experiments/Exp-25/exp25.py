from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the decision tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Accuracy on the test data
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model accuracy on test data: {accuracy * 100:.2f}%\n")

# Inputs for the new flower
sepal_length = float(input("Enter sepal length (cm): "))
sepal_width = float(input("Enter sepal width (cm): "))
petal_length = float(input("Enter petal length (cm): "))
petal_width = float(input("Enter petal width (cm): "))

# Predict the species
new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(new_flower)[0]

print(f"\nPredicted species: {iris.target_names[prediction]}")
