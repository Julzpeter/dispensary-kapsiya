from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('', views.home_view, name="home_view"),
    path('adminclick/', views.adminclick_view),
    path('adminlogin/', views.sign_in, name='login'),
    path('adminsignup/', views.admin_signup_view, name='adminsignup'),
    path('afterlogin/', views.afterlogin_view,name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='index.html'),name='logout'),

]