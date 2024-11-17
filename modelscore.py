import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import joblib

# Load the dataset
try:
    data = pd.read_csv('ml_model/blood_cancer_data.csv')
except FileNotFoundError:
    raise FileNotFoundError("The dataset 'blood_cancer_data.csv' was not found. Ensure it's in the correct directory.")

# Convert categorical attributes to numerical
data['blood_type'] = data['blood_type'].astype('category').cat.codes
data['hla_typing'] = data['hla_typing'].astype('category').cat.codes

# Features and target variable
X = data[['age', 'blood_type', 'hla_typing']]
y = data['compatible']

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate KNN for multiple K values
k_values = range(1, 21)
accuracy_test = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracy_test.append(knn.score(X_test, y_test))

# Save the best KNN model based on test accuracy
best_k = k_values[np.argmax(accuracy_test)]
knn_best = KNeighborsClassifier(n_neighbors=best_k)
knn_best.fit(X_train, y_train)

try:
    joblib.dump(knn_best, 'ml_model/knn_model.pkl')
except Exception as e:
    raise IOError(f"Error saving the model: {e}")

# Evaluate and print metrics
y_pred = knn_best.predict(X_test)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Plotting KNN performance
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_test, label='Test Accuracy', marker='o')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy for Different K Values')
plt.legend()
plt.grid(True)
plt.show()