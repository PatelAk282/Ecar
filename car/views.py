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
    template_name = 'car/cartypecreate.html'
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
    template_name = 'car/cartypecreate.html'
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

class FuelCreationView(CreateView):
    form_class = FuelCreationForm
    model = Fuel
    template_name = 'car/fuelcreate.html'
    success_url = '/car/list_fuel/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class FuelListView(ListView):
    model = Fuel
    template_name = 'car/fuel_list.html'
    context_object_name = 'fuel_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class FuelUpdateView(UpdateView):
    model = Fuel
    form_class = FuelCreationForm
    template_name = 'car/fuelcreate.html'
    success_url = '/car/list_fuel/'
    

      
class FuelDeleteView(DeleteView):
    model = Fuel
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_fuel/'


class BrandCreationView(CreateView):
    form_class = BrandCreationForm
    model = Brand
    template_name = 'car/brandcreate.html'
    success_url = '/car/list_brand/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class BrandListView(ListView):
    model = Brand
    template_name = 'car/brand_list.html'
    context_object_name = 'brand_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandCreationForm
    template_name = 'car/brandcreate.html'
    success_url = '/car/list_brand/'
    

      
class BrandDeleteView(DeleteView):
    model = Brand
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_brand/'

class ExteriorCreationView(CreateView):
    form_class = ExteriorCreationForm
    model = Exterior
    template_name = 'car/exteriorcreate.html'
    success_url = '/car/list_exterior/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class ExteriorListView(ListView):
    model = Exterior
    template_name = 'car/exterior_list.html'
    context_object_name = 'exterior_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class ExteriorUpdateView(UpdateView):
    model = Exterior
    form_class = ExteriorCreationForm
    template_name = 'car/exteriorcreate.html'
    success_url = '/car/list_exterior/'
    

      
class ExteriorDeleteView(DeleteView):
    model = Exterior
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_exterior/'

class ComfortCreationView(CreateView):
    form_class = ComfortCreationForm
    model = Comfort
    template_name = 'car/comfortcreate.html'
    success_url = '/car/list_comfort/'
    
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class ComfortListView(ListView):
    model = Comfort
    template_name = 'car/comfort_list.html'
    context_object_name = 'comfort_list'
    
    def get_queryset(self):
        return super().get_queryset()    
    

class ComfortUpdateView(UpdateView):
    model = Comfort
    form_class = ComfortCreationForm
    template_name = 'car/comfortcreate.html'
    success_url = '/car/list_comfort/'
    

      
class ComfortDeleteView(DeleteView):
    model = Comfort
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
    success_url = '/car/list_comfort/'
