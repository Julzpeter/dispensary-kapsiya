"""dispensary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from kapsiya import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    #----------------ADMIN RELATED URLS
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),
    
    #url patterns for the navbar
    path('adminclick/', views.adminclick_view),
    path('doctorclick/', views.doctorclick_view),  
    path('patientclick/', views.patientclick_view),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),

    #url for signup 
    path('adminsignup/', views.admin_signup_view, name='adminsignup'),
    path('adminsignup/adminlogin/', LoginView.as_view(template_name='adminlogin.html')),
    path('adminsignup/adminlogin/adminsignup', views.admin_signup_view, name='adminsignup'),
    path('doctorsignup/', views.doctor_signup_view, name='doctorsignup'),
    path('doctorsignup/doctorlogin/', LoginView.as_view(template_name='doctorlogin.html')), 
    path('doctorsignup/doctorlogin/doctorsignup', views.doctor_signup_view, name='doctorsignup'),
    path('patientsignup/', views.patient_signup_view, name='patientsignup'),
    path('patientsignup/patientlogin/', LoginView.as_view(template_name='patientlogin.html')), 

    #urls for login
    path('doctorlogin/', LoginView.as_view(template_name='doctorlogin.html')), 
    path('adminlogin/', LoginView.as_view(template_name='adminlogin.html')),
    path('adminlogin/adminsignup', views.admin_signup_view, name='adminsignup'),
    path('patientlogin/', LoginView.as_view(template_name='patientlogin.html')),
    #path('patientlogin/patientsignup', views.patient_signup_view, name='patientsignup'),
    path('patientsignup/patientlogin/patientsignup/', views.patient_signup_view, name='patientsignup'),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='index2.html'),name='logout'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    #url for the side bar for the doctor
    path('admin-doctor', views.admin_doctor_view, name='admin-doctor'),
    path('admin-view-doctor', views.admin_view_doctor_view, name='admin-view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('admin-add-doctor',views.admin_add_doctor_view, name='admin-add-doctor'),
    path('admin-approve-doctor', views.admin_approve_doctor_view,name='admin-approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),

    #url for the side bar for the patient
    path('admin-patient', views.admin_patient_view, name='admin-patient'),
    path('admin-view-patient',views.admin_view_patient_view, name='admin-view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('admin-add-patient', views.admin_add_patient_view,name='admin-add-patient'),
    path('admin-approve-patient', views.admin_approve_patient_view,name='admin-approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('admin-discharge-patient', views.admin_discharge_patient_view,name='admin-discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('download-pdf/<int:pk>', views.download_pdf_view,name='download-pdf'),
    #url for the side bar for the appointment
    path('admin-appointment',views.admin_appointment_view, name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_views,name='admin-add-appointment'),#added the s after view to differentiate it from the new url
    path('add-appointment', views.admin_add_appointment_view,name='add-appointment'),#the new urls for the index page, for visitors
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    
]

#-----------DOCTOR RELATED URLS
urlpatterns +=[
    #url patterns for the side bar(patients)
    path('doctor-dashboard',views.doctor_dashboard_view, name='doctor-dashboard'),
    path('search', views.search_view,name='search'),
    #path('doctor-discharge-patient', views.doctor_discharge_patient_view,name='doctor-discharge-patient'),
    #path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
    path('doctor-patient', views.doctor_patient_view,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient_view,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient_view,name='doctor-view-discharge-patient'),

    #url patterns for the side bar (appointments)
    path('doctor-appointment', views.doctor_appointment_view,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment_view,name='doctor-view-appointment'),
    #path('doctor-add-appointment', views.doctor_add_appointment_view,name='doctor-add-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment_view,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment_view,name='delete-appointment'),
]

#----------FOR PATIENT RELATED URLS--------------------------
urlpatterns +=[
    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
]
