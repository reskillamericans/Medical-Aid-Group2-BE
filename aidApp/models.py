from django.db import models
from datetime import datetime
from django.utils import timezone

class Doctors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    clinic = models.CharField(max_length=50)
    pharmacy = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name

class Clinics(models.Model):
    clinic_name = models.CharField(max_length=50)
    open_hours = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.clinic_name

class Pharmacies(models.Model):
    pharmacy_name = models.CharField(max_length=50)
    open_hours = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.pharmacy_name

class Patients(models.Model):
    first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    doctor_last_name = models.ForeignKey(Doctors, null=True, on_delete=models.SET_NULL)
    clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
    pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}  {self.patient_last_name}"

# class Admin(models.Model):
#     admin_full_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
#     pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    
#     def __str__(self):
#         return self.admin_full_name

class Consultations(models.Model):
    last_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_last_name = models.ForeignKey(Patients, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
    pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    consultation_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.patient_last_name}"

class Feedback_Complaint(models.Model):
    patient_first_name = models.ForeignKey(Patients, on_delete=models.CASCADE)
    feedback_or_complaint = models.CharField(max_length=10)
    patient_message = models.CharField(max_length=200)
    admin_reply = models.CharField(max_length=200)

    def __str__(self):
        return self.feedback_or_complaint

class FAQ(models.Model):
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)

    def __str__(self):
        return self.question 