from django.urls import path
from vehicle import views

urlpatterns = [
    path('', views.VehicleList.as_view(), name="vehicle-list"),
    path('similer-vehicle/', views.SimilerVehilceList.as_view(), name="similer-vehicle-list"),
]