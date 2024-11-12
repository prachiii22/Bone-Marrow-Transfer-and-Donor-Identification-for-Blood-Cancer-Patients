from django.urls import path
from . import views

urlpatterns = [
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('predict_compatibility/', views.predict_compatibility, name='predict_compatibility'),
]