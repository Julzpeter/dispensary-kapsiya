from django.contrib import admin
from django.contrib import admin
from .models import Nurse,Patient,Appointment
# Register your models here.
class NurseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nurse, NurseAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

