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
    
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),
    

    path('adminclick/', views.adminclick_view),
    
    path('adminsignup/', views.admin_signup_view, name='adminsignup'),

    path('adminlogin/', LoginView.as_view(template_name='adminlogin.html')),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='index.html'),name='logout'),

    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    #url for the side bar for the doctor
    path('admin-doctor', views.admin_doctor_view, name='admin-doctor'),
     #url for the side bar for the patient
    path('admin-patient', views.admin_patient_view, name='admin-patient'),
    #url for the side bar for the appointment
    path('admin-appointment',views.admin_appointment_view, name='admin-appointment'),


   
    
]
