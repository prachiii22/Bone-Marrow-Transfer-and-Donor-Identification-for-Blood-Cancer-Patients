import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import joblib

# Load the dataset
data = pd.read_csv('ml_model/blood_cancer_data.csv')

# Convert categorical attributes to numerical
data['blood_type'] = data['blood_type'].astype('category').cat.codes
data['hla_typing'] = data['hla_typing'].astype('category').cat.codes

# Features and target variable
X = data[['age', 'blood_type', 'hla_typing']]
y = data['compatible']

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)
X
y.shape

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.shape
X_test.shape

# applying knn algo
from sklearn.neighbors import KNeighborsClassifier
KNN = KNeighborsClassifier()

model = KNN.fit(X_train,y_train)

# accuracy of the model
model.score(X_train , y_train)

k_values = range(1, 21)  # Test K values from 1 to 20
accuracy_test = []

# Train and evaluate KNN for multiple K values
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracy_test.append(knn.score(X_test, y_test))
    
# Plotting KNN performance
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_test, label='Test Accuracy', marker='o', color='b')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Accuracy')
plt.title('KNN Accuracy for Different K Values')
plt.legend()
plt.grid(True)
plt.show()

# Save the trained model
import pickle as pkl
with open('minorprojectknn.pkl' , 'wb') as f:
    pkl.dump(model,f)
