from django.shortcuts import render, redirect
from .models import Patient, Donor
from django.http import JsonResponse
import numpy as np
import joblib
import pandas as pd

# Load the trained KNN model
knn_model = joblib.load('ml_model/knn_model.pkl')

def home(request):
    return render(request, 'home.html')

def add_patient(request):
    if request.method == 'POST':
        patient = Patient(
            name=request.POST['name'],
            age=int(request.POST['age']),
            gender=request.POST['gender'],
            blood_type=request.POST['blood_type'],
            diagnosis_date=request.POST['diagnosis_date'],
            cancer_type=request.POST['cancer_type'],
            treatment_history=request.POST['treatment_history'],
            current_treatment=request.POST['current_treatment'],
            hla_typing=request.POST['hla_typing'],
            contact_info=request.POST['contact_info'],
        )
        patient.save()
        return JsonResponse({'message': 'Patient added successfully.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def add_donor(request):
    if request.method == 'POST':
        donor = Donor(
            name=request.POST['name'],
            age=int(request.POST['age']),
            gender=request.POST['gender'],
            blood_type=request.POST['blood_type'],
            hla_typing=request.POST['hla_typing'],
            health_status=request.POST['health_status'],
            contact_info=request.POST['contact_info'],
            availability_for_donation=request.POST['availability_for_donation'] == 'True',
        )
        donor.save()
        return JsonResponse({'message': 'Donor added successfully.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def predict_compatibility(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        blood_type = request.POST['blood_type']
        hla_typing = request.POST['hla_typing']

        # Use ML model for prediction
        patient_data = {
            'blood_type': ['A', 'B', 'O', 'AB'],
            'hla_typing': ['HLA-A1', 'HLA-B8', 'HLA-DR3', 'HLA-DQ4']
        }
        blood_type_encoded = patient_data['blood_type'].index(blood_type)
        hla_typing_encoded = patient_data['hla_typing'].index(hla_typing)
        input_data = np.array([[age, blood_type_encoded, hla_typing_encoded]])
        prediction = knn_model.predict(input_data)

        message = "Compatible" if prediction[0] else "Not Compatible"
        details = {'Age': age, 'Blood Type': blood_type, 'HLA Typing': hla_typing}

        # Retrieve patient and donor details for display
        patient = Patient.objects.get(age=age, blood_type=blood_type, hla_typing=hla_typing)  # Add appropriate filters
        donor = Donor.objects.filter(blood_type=blood_type, hla_typing=hla_typing, availability_for_donation=True).first()

        return render(request, 'result.html', {'message': message, 'details': details, 'patient': patient, 'donor': donor})

    return redirect('home')