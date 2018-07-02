from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import re
import bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.

def index(request):
    if "user_id" in request.session:
        return redirect("/home")
    return render(request, "bookreviews/index.html")

def register(request):
    if request.method != "POST":
        return redirect("/")
    error = False
    name = request.POST["name"]
    alias = request.POST["alias"] 
    email = request.POST["email"]
    pw = request.POST["password"]
    cfpw = request.POST["cfpw"]
    if len(name) < 2:
        error = True
        messages.error(request,"Name must be longer than 2 characters")
    if any(char.isdigit() for char in name):
        error = True
        messages.error(request, "Name cannot contain digit")        
    if len(alias) < 2:
        error = True
        messages.error(request,"Alias must be longer than 2 characters")
    if any(char.isdigit() for char in alias):
        error = True
        messages.error(request, "ALias cannot contain digit")              
    if len(name) < 2:
        error = True
        messages.error(request,"Name must be longer than 2 characters")
    if not EMAIL_REGEX.match(email):
        error = True
        messages.error(request,"Invalid Email Address")
    if len(pw) < 8:
        error = True
        messages.error(request,"Password must be at least 8 characters")
    if pw != cfpw:
        error = True
        messages.error(request,"Confirmation password doesn't match")
    if User.objects.filter(email=email):
        error = True
        messages.error(request, "Email already exist, please log in")    
    print messages
    if error:
        return redirect("/")
    hp = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    this_user = User(first_name=name, email=email, password = hp)
    this_user.save()
    request.session["user_id"] = this_user.id
    return redirect("/home")


def login(request):
    error = False
    if request.method != "POST":
        return redirect("/")
    if not User.objects.filter(email = request.POST["email"]):
        error = True
        messages.error(request,"Email is not in the system")
    else:
        this_user = User.objects.get(email=request.POST["email"])
        if not bcrypt.checkpw(request.POST["password"].encode(), this_user.password.encode()):
            error = True
            messages.error(request,"Password is wrong")  
    if error:
        return redirect("/")
    request.session["user_id"] = this_user.id    
    return redirect("/home")        
    
def home(request):
    this_user = User.objects.get(id = request.session["user_id"])
    context = {
        "uploads" : this_user.uploaded_books.all(),
        "allreviews" : Review.objects.all(),
        "reviews": this_user.contents.all()

    }
    return render(request, "bookreviews/home.html", context)

def addpage(request):
    return render(request, "bookreviews/add.html")


def add(request):
    if request.method != "POST": 
        return redirect("/home")
    # reviews rely on book shtne create book first
    this_book = Book(title = request.POST["title"], author = request.POST["author"], uploader = User.objects.get(id=request.session["user_id"]))
    this_book.save()
    this_review = Review(content = request.POST["review"], rating = request.POST["rating"], reviewed_by = User.objects.get(id=request.session["user_id"]), book_reviewed = this_book)
    this_review.save()
    return redirect("/home")

def bookpage(request, book_id):
    this_book = Book.objects.get(id = book_id)
    context = {
        "this_book": this_book,
        "book_reviews": this_book.reviews.all(),
    }
    return render(request, "bookreviews/book.html", context)



def addreview(request, book_id):
    if request.method != "POST": 
        return redirect("/home")
    this_book = Book.objects.get(id=book_id)    
    this_review = Review(content = request.POST["review"], rating = request.POST["rating"], reviewed_by = User.objects.get(id=request.session["user_id"]), book_reviewed = this_book)
    this_review.save()
    return redirect("/home")



def user(request, user_id):
    context = {
        "alias": User.objects.get(id=user_id),
        "reviews": User.objects.get(id=user_id).contents.all()
    }
    return render(request, "bookreviews/user.html", context)

def logout(request):
    request.session.clear()
    return redirect("/")
