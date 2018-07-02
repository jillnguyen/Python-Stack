from django.shortcuts import render, redirect
from datetime import datetime
from models import *

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "mycourse/index.html" , context)

def add(request):
    if request.method != "POST":
        return redirect("/")
    this_course = Course(name = request.POST["name"], desc = request.POST["desc"])
    this_course.save()
    return redirect("/")


def delete(request, id):
    context = {
        "this_course": Course.objects.get(id=id)
    }
    return render(request,"mycourse/delete.html", context)


def confirm(request, id):
    this_user = Course.objects.get(id=id)
    this_user.delete()
    return redirect("/")

