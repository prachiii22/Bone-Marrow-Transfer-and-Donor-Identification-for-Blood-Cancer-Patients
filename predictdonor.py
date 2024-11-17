import numpy as np
import joblib

# Load the trained KNN model
try:
    knn_model = joblib.load('ml_model/knn_model.pkl')
except FileNotFoundError:
    raise FileNotFoundError("The KNN model file 'knn_model.pkl' was not found. Ensure the model is trained and saved.")

def predict_compatibility(age, blood_type, hla_typing, patient_data):
    """
    Predicts donor compatibility based on age, blood type, and HLA typing.

    Args:
        age (int): Age of the patient or donor.
        blood_type (str): Blood type (e.g., 'A', 'B').
        hla_typing (str): HLA typing (e.g., 'A1', 'B8').
        patient_data (DataFrame): Reference dataset with categorical encodings.

    Returns:
        bool: True if compatible, False otherwise.
    """
    try:
        # Encode blood_type and hla_typing
        blood_type_encoded = patient_data['blood_type'].cat.categories.get_loc(blood_type)
        hla_typing_encoded = patient_data['hla_typing'].cat.categories.get_loc(hla_typing)

        # Prepare input for prediction
        input_data = np.array([[age, blood_type_encoded, hla_typing_encoded]])
        prediction = knn_model.predict(input_data)

        # Interpret prediction result
        return bool(prediction[0])
    except KeyError as e:
        print(f"KeyError: {e}. Ensure valid input for blood type and HLA typing.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None