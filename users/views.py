from django.contrib.auth import login, authenticate, logout
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SignUpForm,ProfileCReationForm
from django.urls import reverse
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('Home')

def sign_up(request):
    form = SignUpForm()
    return render(request,'users/signup.html',{
        "form" : form,
        "page":"sign up"
    })

def createuser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()
            print(user.username,user.email)
            raw_password = form.cleaned_data.get('password1')
            user  = authenticate(username = user.username ,password=raw_password)
            auth.login(request,user)
            form = ProfileCReationForm()
            return render(request,"users/profile_create.html",{
                "page":"profile_creation",
                "form":form,
                "page":"Create profile"
            })
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form,"page":"signu up"})


def login(request):
    
    return render(request,'users/login.html',{
        "page":"login"
    })
    
def handle_login(request):
    if request.method == "POST":
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username = username,password=raw_password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('index')
        else:
            return HttpResponse("invalid credentials")
    else:
        return HttpResponse("not allowed")

def logout(request):
    auth.logout(request)
    return redirect('Home')

def createprofile(request):
    if request.method == "POST":
       form = ProfileCReationForm(request.POST)
       if form.is_valid():
           request.user.profile.reg_no = form.cleaned_data.get('reg_no')
           request.user.profile.Branch = form.cleaned_data.get('Branch')
           request.user.profile.Year = form.cleaned_data.get('Year')
           request.user.save()
           
           return redirect('Home')