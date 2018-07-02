from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not "counter" in request.session:
        request.session["counter"] = 1
    if not "randomword" in request.session:
        request.session["randomword"] = "" 
    print request.session["randomword"]   
    context = {
        "counter": request.session["counter"],
        "randomstr": request.session["randomword"]
    }
    return render(request,"randomword/index.html", context)    

def process(request):
    request.session["counter"] += 1
    # randomword = get_random_string(14)
    request.session["randomword"] = get_random_string(14)
    return redirect("/")
