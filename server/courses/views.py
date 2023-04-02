from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def course(request):
    return render(request, 'courses/course.html')


def deep_learning(request):
    return HttpResponse('Welcome to Deep_learning course')


def data_science(request):
    return HttpResponse('Welcome to Data_science')


def machine_learning(request):
    return HttpResponse('Welcome to Machine learning')
