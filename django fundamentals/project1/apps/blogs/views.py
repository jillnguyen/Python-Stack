# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    response = "placeholder to display blog " + number
    return HttpResponse(response)

def edit(request, number):
    response = "placeholder to edit blog " + number
    return HttpResponse(response)

def delete(request, number):
    return redirect("/")