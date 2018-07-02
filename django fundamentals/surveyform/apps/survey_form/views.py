from django.shortcuts import render

# Create your views here.
def index(request):
    if not "name" in request.session:
        request.session["name"] = ""
    if not "language" in request.session:
        request.session["language"] = ""
    if not "location" in request.session:
        request.session["location"] = ""
    if not "comment" in request.session:
        request.session["comment"] = ""            
    return render(request,"survey_form/index.html")

def process(request):
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["language"] = request.POST["language"]
    request.session["comment"] = request.POST["comment"]
    context = {
        "name": request.session["name"], 
        "language": request.session["language"],
        "location": request.session["location"],
        "comment": request.session["comment"],
    }
    return render(request,"survey_form/process.html", context)