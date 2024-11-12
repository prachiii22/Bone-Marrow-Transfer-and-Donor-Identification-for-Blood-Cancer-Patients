import pickle

def predict_donor(hla_match, age_diff):
    with open('ML_model/knn_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict([[hla_match, age_diff]])[0]

# Example usage
hla_match = 0.85
age_diff = 6
result = predict_donor(hla_match, age_diff)
print("Compatible" if result == 1 else "Not Compatible")