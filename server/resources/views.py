from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def free_cources(request):
    return render(request, 'resources/resource.html')
