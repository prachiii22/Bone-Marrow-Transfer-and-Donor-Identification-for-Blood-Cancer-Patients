from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Patient, Donor
import numpy as np
import joblib

# Load the trained KNN model
knn_model = joblib.load('ml_model/knn_model.pkl')

def home(request):
    return render(request, 'home.html')

# This view renders the result page
def result_page(request):
    return render(request, 'result.html')

@csrf_exempt
def add_patient(request):
    if request.method == 'POST':
        try:
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
            return redirect('home')  # Redirect to home after successful addition
        except Exception as e:
            return render(request, 'home.html', {'error': f'Error adding patient: {str(e)}'})
    return redirect('home')

@csrf_exempt
def add_donor(request):
    if request.method == 'POST':
        try:
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
            return redirect('home')  # Redirect to home after successful addition
        except Exception as e:
            return render(request, 'home.html', {'error': f'Error adding donor: {str(e)}'})
    return redirect('home')

def predict_compatibility(request):
    if request.method == 'POST':
        try:
            # Get form data
            age = int(request.POST.get('age'))
            blood_type = request.POST.get('blood_type')
            hla_typing = request.POST.get('hla_typing')

            # Validate inputs
            if not all([age, blood_type, hla_typing]):
                return render(request, 'result.html', {
                    'error': 'All fields are required'
                })

            # Use ML model for prediction
            patient_data = {
                'blood_type': ['A', 'B', 'O', 'AB'],
                'hla_typing': ['HLA-A1', 'HLA-B8', 'HLA-DR3', 'HLA-DQ4']
            }

            try:
                blood_type_encoded = patient_data['blood_type'].index(blood_type.upper())
                hla_typing_encoded = patient_data['hla_typing'].index(f'HLA-{hla_typing.upper()}')
            except ValueError:
                return render(request, 'result.html', {
                    'error': 'Invalid blood type or HLA typing'
                })

            # Load model and predict
            knn_model = joblib.load('ml_model/knn_model.pkl')
            input_data = np.array([[age, blood_type_encoded, hla_typing_encoded]])
            prediction = knn_model.predict(input_data)

            message = "Compatible" if prediction[0] else "Not Compatible"
            details = {'Age': age, 'Blood Type': blood_type, 'HLA Typing': hla_typing}

            # Get matching records
            patient = Patient.objects.filter(blood_type=blood_type).first()
            donor = Donor.objects.filter(blood_type=blood_type, availability_for_donation=True).first()

            return render(request, 'result.html', {
                'message': message,
                'details': details,
                'patient': patient,
                'donor': donor
            })

        except Exception as e:
            return render(request, 'result.html', {'message': f'Error: {str(e)}'})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
