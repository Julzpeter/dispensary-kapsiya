from django.shortcuts import render, redirect
from .forms import AdminSignUpForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from . import models
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render (request, 'index.html')

##view function for showinng the signup/login button for the admin
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'adminclick.html')
"""
def sign_in(request):
    if request.method == 'GET':
        form = AdminLoginForm()
        return render(request, 'adminlogin.html', {'form':form})

    elif request.method == 'POST':
        form = AdminLoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return HttpResponseRedirect('admin-dashboard')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'adminlogin.html',{'form': form})
"""
def admin_signup_view(request):
    if request.method == 'GET':
        form = AdminSignUpForm()
        return render(request, 'adminsignup.html', {'form': form})  
    if request.method == 'POST':
            form = AdminSignUpForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                my_admin_group = Group.objects.get_or_create(name='ADMIN')
                my_admin_group[0].user_set.add(user)
                messages.success(request, 'You have singed up successfully.')
                return HttpResponseRedirect('adminlogin')
    return render(request,'adminsignup.html', {'form': form})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'doctor_wait_for_approval.html')
    elif is_patient(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('patient-dashboard')
    else:
        return render(request,'patient_wait_for_approval.html')

## ADMIN RELATED VIEWS 
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    nurses=models.Nurse.objects.all().order_by('-id')
    patients=models.Patient.objects.all().order_by('-id')
    #for three cards
    nursecount=models.Nurse.objects.all().filter(status=True).count()
    pendingnursecount=models.Nurse.objects.all().filter(status=False).count()

    patientcount=models.Patient.objects.all().filter(status=True).count()
    pendingpatientcount=models.Patient.objects.all().filter(status=False).count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    'nurses':nurses,
    'patients':patients,
    'nursecount':nursecount,
    'pendingnursecount':pendingnursecount,
    'patientcount':patientcount,
    'pendingpatientcount':pendingpatientcount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'admin_dashboard.html',context=mydict)

##VIEWS FOR THE SIDE BAR ON THE ADMIN DASHBOARD
@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request, 'admin_doctor.html')