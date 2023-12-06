from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from myapp.models import *
from myapp.form import *

def home(request):
    return render(request,'bas.html')

def signup1(request):
    if request.method=='POST':
        username=request.POST.get("Username")
        email=request.POST.get("Email")
        password1=request.POST.get('Password1')
        password2=request.POST.get('Password2')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists')
                print('already have')
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(user_login)
        else:
            print('wrong password')
    return render(request,'signup1.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST.get("Username")
        password1=request.POST.get('Password1')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            messages.info(request,"user not exist")
            print('usre not exist')
            return redirect(user_login)
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect(user_login)

def book_form(request):
    form=bookform()
    if request.method=='POST':
        form=bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(list_book)
    return render(request,'book_form.html',{'form':form})

def list_book(request):
    index=book.objects.all()
    return render(request,'book_list.html',{'list':index})