# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request,"login_registration/index.html")

def registration(request):
    error = False
    if request.method != "POST":
        return redirect("/")
    first = request.POST["first_name"]
    last = request.POST["last_name"]    
    email = request.POST["email"]    
    passw = request.POST["pw"]
    confirm = request.POST["cfpw"]
    if len(first) < 2:
        error = True
        messages.error(request, "First name must be longer than 2 character")
    if any(char.isdigit() for char in first):
        error = True
        messages.error(request, "First name cannot contain digit")
    if len(last) < 2:
        error = True
        messages.error(request, "Last name must be longer than 2 character")
    if any(char.isdigit() for char in last):
        error = True
        messages.error(request, "Last name cannot contain digit")
    if len(passw) < 8:
        error = True
        messages.error(request, "Password must be at least 8 characters")
    if passw != confirm :
        error = True
        messages.error(request, "Password and confirmation must match")
    if not EMAIL_REGEX.match(email):
        error = True
        messages.error(request, "Invalid email address")


    if User.objects.filter(email=request.POST["email"]):
        error = True
        messages.error(request, "Email already exist, please log in")    
    if error:
        return redirect("/")

    hp  = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
    this_user = User.objects.create(first_name = first, last_name = last, email = email, password = hp )
    request.session["id"] = this_user.id
    request.session["name"] = this_user.first_name
    return redirect("/success")   

def login(request):
    error = False
    if request.method != "POST":
        return redirect("/")   
    passw = request.POST["pw"]
    if not User.objects.filter(email=request.POST["email"]):
        error = True
        messages.error(request, "Email doesn't exist. Please register")
    else:
        if not bcrypt.checkpw(passw.encode(), the_user.password.encode()):
            error = True
            messages.error(request, "You entered the wrong password")
    if error:
        return redirect("/")
    the_user = User.objects.get(email=request.POST["email"])
    request.session["name"] = the_user.first_name      
    return redirect("/success")

def success(request):
    return render(request,"login_registration/success.html")
         
