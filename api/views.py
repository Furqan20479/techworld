from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'techworld/index.html')

def four_0_four(request):
    return render(request, 'techworld/404.html')

def about(request):
    return render(request, 'techworld/about.html')

def appointment(request):
    return render(request, 'techworld/appointment.html')

def contact(request):
    return render(request, 'techworld/contact.html')

def feature(request):
    return render(request, 'techworld/feature.html')

def service(request):
    return render(request, 'techworld/service.html')

def team(request):
    return render(request, 'techworld/team.html')
