from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Doctors, Clinics, Pharmacies, Patients, Consultations, Feedback_Complaint, FAQ

admin.site.register(Doctors)
admin.site.register(Clinics)
admin.site.register(Pharmacies)
admin.site.register(Patients)
admin.site.register(Consultations)
admin.site.register(Feedback_Complaint)
admin.site.register(FAQ)