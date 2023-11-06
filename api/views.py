from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def signup(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')        

        print(username, email, password, confirmpassword)
        
        user = User.objects.create_user(username=username, email=email, password=password, confirmpassword=confirmpassword)
        return render(request, 'api/templates/api/login.html')


    return render(request, 'api/signup.html')

def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("LoggedIn")
        else:
            return HttpResponse("Invalid credentials")
    return HttpResponse("GET REQUEST")

        

    

def index(request):
    return render(request, 'api/index.html')


def four_0_four(request):
    return render(request, 'api/404.html')


def about(request):
    return render(request, 'api/about.html')


def appointment(request):
    return render(request, 'api/appointment.html')


def contact(request):
    return render(request, 'api/contact.html')


def feature(request):
    return render(request, 'api/feature.html')


def service(request):
    return render(request, 'api/service.html')


def team(request):
    return render(request, 'api/team.html')

def testimonial(request):
    return render(request, 'api/testimonial.html')
