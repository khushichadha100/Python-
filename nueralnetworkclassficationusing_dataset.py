import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.neural_network import MLPClassifier

# Load the Iris dataset
X, y = load_iris(return_X_y=True)

# One-hot encode the target variable
y = OneHotEncoder(sparse=False).fit_transform(y.reshape(-1, 1))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create MLPClassifier model
model = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)

# Calculate accuracy
correct = 0
for pred, true in zip(predictions, y_test):
    if np.array_equal(pred, true):
        correct += 1

# Calculate and print accuracy
accuracy = correct / len(y_test)
print("Test Accuracy:", accuracy)
