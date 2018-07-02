from django.shortcuts import render, redirect
import random
import datetime
# Create your views here.
def index(request):
    if not "gold" in request.session:
        request.session["gold"] = 0
        request.session["log"] = []
    return render(request,'ninja_gold/index.html')

def process(request,loc):
    if request.method != "POST":
        return redirect("/")
    if loc == "farm":
        gold = random.randrange(10,21)
        logstr = ("gain", "Earn {} gold from {} ({})".format(gold, loc, datetime.datetime.now()))
    if loc == "cave":
        gold = random.randrange(5,11)
        logstr = ("gain", "Earn {} gold from {} ({})".format(gold, loc, datetime.datetime.now()))

    if loc == "house":
        gold = random.randrange(2,6)
        logstr = ("gain", "Earn {} gold from {} ({})".format(gold, loc, datetime.datetime.now()))

    if loc == "casino":
        gold = random.randrange(-50,51)
        if gold >= 0:
            logstr = ("gain", "Earn {} gold from {} ({})".format(gold, loc, datetime.datetime.now()))
        else:
            logstr = ("loss", "Lost {} gold from {} ({})".format(abs(gold), loc, datetime.datetime.now()))

    request.session["gold"] += gold
    request.session["log"].insert(0,logstr)
    print request.session["gold"]
    print request.session["log"]
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")