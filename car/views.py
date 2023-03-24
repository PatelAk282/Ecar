from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView
from .models import *

# Create your views here.

def home(request):
    return render(request,'user/home.html')

class CartypeCreationView(CreateView):
    form_class = CartypeCreationForm
    model = Cartype
    template_name = 'car/cartypecreation.html'
    success_url = '/car/list_cartype/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class CartypeListView(ListView):
    model = Cartype
    template_name = 'car/cartype_list.html'
    context_object_name = 'cartype_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class CartypeUpdateView(UpdateView):
    model = Cartype
    form_class = CartypeCreationForm
    template_name = 'car/cartypecreation.html'
    success_url = '/car/list_cartype/'
    
# class CartypeDetailView(DetailView):
#     model = Cartype
#     template_name = 'car/cartype_detail.html'
#     context_object_name = 'project_detail'
    
      
class CartypeDeleteView(DeleteView):
    model = Cartype
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_cartype/'
      

class CarvarientCreationView(CreateView):
    form_class = CarvarientCreationForm
    model = Carvarient
    template_name = 'car/carvarientcreate.html'
    success_url = '/car/list_carvarient/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    
class CarvarientListView(ListView):
    model = Carvarient
    template_name = 'car/carvarient_list.html'
    context_object_name = 'carvarient_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class CarvarientUpdateView(UpdateView):
    model = Carvarient
    form_class = CarvarientCreationForm
    template_name = 'car/carvarientcreate.html'
    success_url = '/car/list_carvarient/'
    
# class CarvarientDetailView(DetailView):
#     model = Carvarient
#     template_name = 'car/carvarient_detail.html'
#     context_object_name = 'project_detail'
    
      
class CarvarientDeleteView(DeleteView):
    model = Carvarient
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_carvarient/'


    
class CarengineCreationView(CreateView):
    form_class = CarengineCreationForm
    model = CarEngineandTransmission
    template_name = 'car/carenginecreate.html'
    success_url = '/car/list_carengine/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class CarengineListView(ListView):
    model = CarEngineandTransmission
    template_name = 'car/carengine_list.html'
    context_object_name = 'carengine_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class CarengineUpdateView(UpdateView):
    model = CarEngineandTransmission
    form_class = CarengineCreationForm
    template_name = 'car/carenginecreate.html'
    success_url = '/car/list_carengine/'
    
# class CarvarientDetailView(DetailView):
#     model = Carvarient
#     template_name = 'car/carvarient_detail.html'
#     context_object_name = 'project_detail'
    
      
class CarengineDeleteView(DeleteView):
    model = CarEngineandTransmission
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_carengine/'


    
class CarCreationView(CreateView):
    form_class = CarCreationForm
    model = Car
    template_name = 'car/carcreate.html'
    success_url = '/car/list_car/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'car_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarCreationForm
    template_name = 'car/carcreate.html'
    success_url = '/car/list_car/'
    

      
class CarDeleteView(DeleteView):
    model = Car
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_car/'
