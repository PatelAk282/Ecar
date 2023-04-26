from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import AdminRegisterForm,UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic import ListView
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView
from car.models import *
from django.core.mail import send_mail
from django.conf import settings





# Create your views here.

class AdminRegisterView(CreateView):
    model = User
    form_class = AdminRegisterForm
    template_name = 'user/admin_register.html'
    success_url = '/user/login/'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        if user is not None:
            subject = "CarAdmin...Welcome to my site..."
            message = "You have been register on my website...\n thank you..."
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            login(self.request,user)
        return super(AdminRegisterView,self).form_valid(form)
        

class UserRegisterview(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = '/user/login/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'owner'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        if user is not None:
            subject = "CarOwner...Welcome to my site..."
            message = "You have been register on my website...\n thank you..."
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, from_email, recipient_list)
            login(self.request,user)
        return super(UserRegisterview,self).form_valid(form)

    


class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        if self.request.user.is_authenticated:    
            if self.request.user.is_admin:
                return '/user/admindashboard/'
            else:
                return '/'
            

class AdminDashboardView(ListView):            
    
    def get(self, request, *args, **kwargs):
     car = Car.objects.all().values()
    
        
     return render(request, 'user/admindashboard.html',{
            'ecar':car, 
        })

    template_name = 'dashboard.html'      


class UserDashboardView(ListView):            
    
    def get(self, request, *args, **kwargs):
        # car1 = Car.objects.all()
       # print("./././/",car)
        #car1 = Car.objects.select_related('Fuel').values()
        car1 = Car.objects.all().values('name','price','exterior__wheel','comfort__vanitymirror','image','fuel__fueltype')
        
        print("******",car1)
        # car2 = Car.objects.raw("select * from car")
        # print(car2)

        
        return render(request, 'user/cars.html',{
         'car':car1
     })

    template_name = 'cars.html'  

 
    




