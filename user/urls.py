from django.contrib import admin
from django.urls import path,include
from .views import AdminRegisterView,UserRegisterview,UserLoginView,AdminDashboardView
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('adminregister/',AdminRegisterView.as_view(),name='adminregister'),
    path('userregister/',UserRegisterview.as_view(),name='userregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('admindashboard/',AdminDashboardView.as_view(),name='admindashboard')
    
    ]
