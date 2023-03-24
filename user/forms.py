from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class AdminRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        return user
    
class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2',)
        # widgets={'username': forms.TextInput(attrs={'class': 'login__input', 'type':'text', 'placeholder':'UserName'}),
        #          'password': forms.PasswordInput(attrs={'class': 'login__input', 'type':'password', 'placeholder':'password'}),
        # }

       
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user