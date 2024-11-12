from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Example models (you would need to define these models for the actual implementation)
from .models import Patient, Donor

@csrf_exempt
def add_patient(request):
    if request.method == 'POST':
        try:
            # Parse incoming data
            data = json.loads(request.body)
            
            # Example: Save patient data to the database (replace with your actual model fields)
            patient = Patient(
                name=data.get('name'),
                age=data.get('age'),
                blood_type=data.get('blood_type'),
                medical_history=data.get('medical_history')
            )
            patient.save()
            
            # Return success response
            return JsonResponse({'message': 'Patient added successfully'}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid data format'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    
    return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def add_donor(request):
    if request.method == 'POST':
        try:
            # Parse incoming data
            data = json.loads(request.body)
            
            # Example: Save donor data to the database (replace with your actual model fields)
            donor = Donor(
                name=data.get('name'),
                age=data.get('age'),
                blood_type=data.get('blood_type'),
                contact_info=data.get('contact_info')
            )
            donor.save()
            
            # Return success response
            return JsonResponse({'message': 'Donor added successfully'}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid data format'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid request method'}, status=400)

@csrf_exempt
def predict_compatibility(request):
    if request.method == 'POST':
        try:
            # Parse incoming data
            data = json.loads(request.body)
            
            # Example: Check blood type and HLA compatibility
            patient_blood_type = data.get('patient_blood_type')
            donor_blood_type = data.get('donor_blood_type')
            
            # Simplified compatibility logic: Blood type compatibility check
            blood_compatible = patient_blood_type == donor_blood_type
            
            # Example: More complex compatibility logic could be added (e.g., HLA matching)
            is_compatible = blood_compatible  # Assume compatibility based only on blood type for simplicity
            
            # Return compatibility result
            return JsonResponse({'success': is_compatible}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid data format'}, status=400)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    
    return JsonResponse({'message': 'Invalid request method'}, status=400)