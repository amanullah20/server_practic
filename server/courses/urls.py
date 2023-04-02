from django.urls import path
from . import views


urlpatterns = [
    path('', views.course),
    path('dep/', views.deep_learning),
    path('math/', views.machine_learning),
    path('data/', views.data_science),


]
