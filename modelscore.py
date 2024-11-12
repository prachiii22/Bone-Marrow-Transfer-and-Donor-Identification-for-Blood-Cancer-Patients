import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Generate synthetic data for demonstration
np.random.seed(0)
num_samples = 500

data = {
    'age': np.random.randint(18, 60, num_samples),
    'blood_type': np.random.choice(['A', 'B', 'AB', 'O'], num_samples),
    'hla_typing': np.random.choice(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], num_samples),
    'availability': np.random.choice(['Yes', 'No'], num_samples),
    'compatible': np.random.choice([0, 1], num_samples)  # 1 for compatible, 0 for incompatible
}

df = pd.DataFrame(data)

# Convert categorical attributes to numerical
df['blood_type'] = df['blood_type'].astype('category').cat.codes
df['hla_typing'] = df['hla_typing'].astype('category').cat.codes
df['availability'] = df['availability'].apply(lambda x: 1 if x == 'Yes' else 0)

# Features and target variable
X = df[['age', 'blood_type', 'hla_typing', 'availability']]
y = df['compatible']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Lists to store accuracy values
k_values = range(1, 21)  # Test different values of K from 1 to 20
accuracy_train = []
accuracy_test = []

# Train and evaluate the KNN model for each value of K
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    
    # Record training and test accuracy
    accuracy_train.append(knn.score(X_train, y_train))
    accuracy_test.append(knn.score(X_test, y_test))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_train, label='Training Accuracy', marker='o')
plt.plot(k_values, accuracy_test, label='Test Accuracy', marker='o')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy for Different Values of K')
plt.legend()
plt.grid(True)
plt.show()

# Choose the best K based on the highest test accuracy
best_k = k_values[np.argmax(accuracy_test)]
knn_best = KNeighborsClassifier(n_neighbors=best_k)
knn_best.fit(X_train, y_train)

# Print accuracy for the best K
print(f"Best K value: {best_k}")
print(f"Training accuracy for K={best_k}: {knn_best.score(X_train, y_train):.2f}")
print(f"Test accuracy for K={best_k}: {knn_best.score(X_test, y_test):.2f}")