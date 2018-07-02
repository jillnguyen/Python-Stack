from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    context = {
        "users" : User.objects.all()
    }    
    return render(request, "semirestful/index.html", context)

def new(request):
    return render(request, "semirestful/new.html")

def edit(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "semirestful/edit.html", context)

def show(request, id):
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "semirestful/show.html", context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iterihtems():
            messages.error(request, error, extra_tags = tag)
            print errors
        return redirect (reverse("my_new"))
    this_user = User(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email = request.POST["email"])    
    this_user.save()
    print this_user.first_name
    return redirect(reverse("my_show",  kwargs={'id': this_user.id }))

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(reverse("my_index"))


def update(request,id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
            print messages
        return redirect("/users/edit")
    else:
        u = User.objects.get(id=id) 
        u.first_name = request.POST["first_name"]
        u.last_name = request.POST["last_name"]
        u.save()            
    return redirect("/users")

