from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=5)
    diagnosis_date = models.DateField()
    cancer_type = models.CharField(max_length=100)
    treatment_history = models.TextField(blank=True)
    current_treatment = models.CharField(max_length=100, blank=True)
    hla_typing = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=5)
    hla_typing = models.CharField(max_length=100)
    health_status = models.CharField(max_length=200, blank=True)
    contact_info = models.CharField(max_length=200)
    availability_for_donation = models.BooleanField(default=True)
