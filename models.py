from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=5)
    diagnosis_date = models.DateField()
    cancer_type = models.CharField(max_length=100)
    treatment_history = models.TextField()
    current_treatment = models.CharField(max_length=100)
    hla_typing = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=5)
    hla_typing = models.CharField(max_length=100)
    health_status = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    availability_for_donation = models.BooleanField()

class TransplantRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    date_of_transplant = models.DateField()
    hla_match_level = models.FloatField()
    success_rate = models.FloatField()
    follow_up_notes = models.TextField()