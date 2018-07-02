from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"haterz/index.html")

def register(request):
    if request.method != "POST":
        return redirect("/")
    result = User.objects.create_user(request.POST)
    if 'errors' in result:
        for error in result["errors"]:
            messages.error(request, error) 
        return redirect("/")
    request.session["user_id"] = result["the_user"].id    
    return redirect("/main")       
    

def login(request):
    if request.method != "POST":
        return redirect("/")
    result = User.objects.login(request.POST)
    if "errors" in result:
        for error in errors:
            messages.error(request, error)
        return redirect("/")
    request.session["user_id"] = result["the_user"].id    
    return redirect("")

def logout(request): 
    request.session.clear()
    return redirect("/")


def main(request):
    if not "user_id" in request.session:
        messages.error(request, "Nice try, SCAM!")
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session["user_id"]),
        "records": Record.objects.all(),
        "my_records": Record.objects.filter(uploader = User.objects.get(id=request.session["user_id"]))
    }
    return render(request,"haterz/main.html", context)


def add(request):
    if not "user_id" in request.session:
        return redirect("/")
    if request.method != "POST":
        return redirect("/")
    Record.objects.add(request.POST,request.session["user_id"])    
    return redirect("/main")

def edit(request, rec_id):
    context = {
        'record': Record.objects.get(id = rec_id)
    }
    return render(request, 'hatez/main.html', context)


def modify(request, rec_id):
    if request.method != "POST":
        return redirect("/main")
    if not "user_id" in request.session:
        return redirect("/")
    record = Record.objects.get(id = rec_id)
    record.album = request.POST["album"]
    record.artist = request.POST["artist"]
    record.label = request.POST["label"]    