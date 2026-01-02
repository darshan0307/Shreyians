from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def home(request):
    return render(request,"index.html")

def login_view(request):
    if request.method == "POST":
        mobile = request.POST.get('mobile')
        login_type = request.POST.get('login_type')

        user = UserLogin.objects.create(
            mobile=mobile,
            login_type=login_type
        )
        if user:
            return redirect('home')
        # return HttpResponse("rigister successfull")
        return redirect('home', user.id)
    
    else:
        return render(request, 'signin.html')

def cource(request):
    return render(request, 'course.html')


def submit(request):
    return redirect("home")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        call_time = request.POST.get('call_time')
        enquiry = request.POST.get('enquiry')

        # For now just printing (later you can save to DB)
        print(name, phone, call_time, enquiry)

        return redirect('home')

    return render(request, 'contact.html')

# def contact_view(request):
#     return redirect('home')

# def success_view(request):
#     return render(request, 'success.html')


# def logout_view(request):
#     logout(request)
#     return redirect('signin')
