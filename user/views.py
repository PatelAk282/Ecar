from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import AdminRegisterForm,UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic import ListView
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView





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
        login(self.request,user)
        return super().form_valid(form)

class UserRegisterview(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user/user_register.html'
    success_url = '/user/login/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        if self.request.user.is_authenticated:    
            if self.request.user.is_admin:
                return '/admin/'
            else:
                return '/'
            

class AdminDashboardView(ListView):            
    
    def get(self, request, *args, **kwargs):
        
        

        return render(request, 'user/dashboard.html')

    template_name = 'dashboard.html'



