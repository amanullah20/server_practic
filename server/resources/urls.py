from django.urls import path
from . import views


urlpatterns = {

    path('re/', views.free_cources)
}
