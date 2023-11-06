from django.shortcuts import render
from api.models import Sign,Log
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.
def signupview(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')        

        user = Sign(username=username, email=email, password=password, confirmpassword=confirmpassword)
        user.save()

        



    return render(request, 'api/signup.html')


def loginview(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            
            login(request,Sign)

            return render(request, 'api/templates/layout/base.html')
        else:
            return HttpResponse("Invalid credentials")
        
    return render(request, "api/login.html")


        