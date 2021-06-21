from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

import os
def path_and_rename(instance, filename):
    upload_to ='Images/'
    ext = filename.split('.')[-1]

    if instance.user.username:
        filename = 'User_Profile_Picture/{}.{}'.format(instance.user.username, ext)
        return os.path.join(upload_to, filename)

class user_profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=700, blank=True)

    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="profile_picture", blank=True)

    patient = "patient"
    health_practitioner = "health_practitioner"
    admin = "admin"

    user_types = [
        (patient, "patient"),
        (health_practitioner, "health_practitioner"),
        (admin, "admin")
    ]
    user_type = models.CharField(max_length=700, choices=user_types, default=patient)


    def __str__(self):
        return self.user.username


=======
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
    patient_first_name = models.CharField(max_length=50)
    patient_last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    doctor_last_name = models.ForeignKey(Doctors, null=True, on_delete=models.SET_NULL)
    clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
    pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name

# class Admin(models.Model):
#     admin_full_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
#     pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    
#     def __str__(self):
#         return self.admin_full_name

class Consultations(models.Model):
    doctor_last_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    patient_last_name = models.ForeignKey(Patients, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinics, null=True, on_delete=models.SET_NULL)
    pharmacy = models.ForeignKey(Pharmacies, null=True, on_delete=models.SET_NULL)
    month = models.CharField(max_length=10)
    date = models.IntegerField
    time = models.CharField(max_length=10)

    def __str__(self):
        return self.patient_last_name

class Feedback_Complaint(models.Model):
    patient_first_name = models.ForeignKey(Patients, on_delete=models.CASCADE)
    feedback_or_complaint = models.CharField(max_length=10)
    patient_message = models.CharField(max_length=200)
    admin_reply = models.CharField(max_length=200)

    def __str__(self):
        return self.feedback_or_complaint
>>>>>>> 108c13a6592282f1e2af35276eb222af270e7f63
