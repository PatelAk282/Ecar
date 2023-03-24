from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('cartype/',CartypeCreationView.as_view(),name='create_cartype'),
    path('list_cartype/',CartypeListView.as_view(),name='cartype_list'),
    path('delete_cartype/<int:pk>',CartypeDeleteView.as_view(),name='delete_cartype'),
    path('update_cartype/<int:pk>',CartypeUpdateView.as_view(),name='update_cartype'),
    # path('detail_cartype/<int:pk>',CartypeDetailView.as_view(),name='detail_cartype')
   

   path('carvarient/',CarvarientCreationView.as_view(),name='create_carvarient'),
   path('list_carvarient/',CarvarientListView.as_view(),name='carvarient_list'),
    path('delete_carvarient/<int:pk>',CarvarientDeleteView.as_view(),name='delete_carvarient'),
    path('update_carvarient/<int:pk>',CarvarientUpdateView.as_view(),name='update_carvarient'),


    path('carengine/',CarengineCreationView.as_view(),name='create_carengine'),
    path('list_carengine/',CarengineListView.as_view(),name='carengine_list'),
    path('delete_carengine/<int:pk>',CarengineDeleteView.as_view(),name='delete_carengine'),
    path('update_carengine/<int:pk>',CarengineUpdateView.as_view(),name='update_carengine'),


    path('car/',CarCreationView.as_view(),name='create_car'),
    path('list_car/',CarListView.as_view(),name='car_list'),
    path('delete_car/<int:pk>',CarDeleteView.as_view(),name='delete_car'),
    path('update_car/<int:pk>',CarUpdateView.as_view(),name='update_car'),

    path('fuel/',FuelCreationView.as_view(),name='create_fuel'),
    path('list_fuel/',FuelListView.as_view(),name='fuel_list'),
    path('delete_fuel/<int:pk>',FuelDeleteView.as_view(),name='delete_fuel'),
    path('update_fuel/<int:pk>',FuelUpdateView.as_view(),name='update_fuel'),

    path('brand/',BrandCreationView.as_view(),name='create_brand'),
    path('list_brand/',BrandListView.as_view(),name='brand_list'),
    path('delete_brand/<int:pk>',BrandDeleteView.as_view(),name='delete_brand'),
    path('update_brand/<int:pk>',BrandUpdateView.as_view(),name='update_brand'),

    path('exterior/',ExteriorCreationView.as_view(),name='create_exterior'),
    path('list_exterior/',ExteriorListView.as_view(),name='exterior_list'),
    path('delete_exterior/<int:pk>',ExteriorDeleteView.as_view(),name='delete_exterior'),
    path('update_exterior/<int:pk>',ExteriorUpdateView.as_view(),name='update_exterior'),

    path('comfort/',ComfortCreationView.as_view(),name='create_comfort'),
    path('list_comfort/',ComfortListView.as_view(),name='comfort_list'),
    path('delete_comfort/<int:pk>',ComfortDeleteView.as_view(),name='delete_comfort'),
    path('update_comfort/<int:pk>',ComfortUpdateView.as_view(),name='update_comfort'),





]




