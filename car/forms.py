from django import forms
from .models import *
from user.models import *

class CartypeCreationForm(forms.ModelForm):
    class Meta:
        model = Cartype
        fields ='__all__'

class CarvarientCreationForm(forms.ModelForm):
    class Meta:
        model = Carvarient
        fields ='__all__'

class CarengineCreationForm(forms.ModelForm):
    class Meta:
        model = CarEngineandTransmission
        fields ='__all__'

class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields ='__all__'