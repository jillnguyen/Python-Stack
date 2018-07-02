from __future__ import unicode_literals

from django.db import models
from datetime import datetime
import bcrypt
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def create_user(self, postData):
        errors = []
    #validations:
        if len(postData["first_name"]) < 2:
            errors.append("First name must be at least 2 characters")
        if len(postData["last_name"]) < 2:
            errors.append("Last name must be at least 2 characters")
        if len(postData["password"]) < 8:
            errors.append("Password must be at least 8 characters")
        if postData["password"] != postData["cfpw"]:
            errors.append("Confirmation password doesn't match")    
        if len(postData["dob"]) == 0:
            errors.append("Birthday required")
        else:
            today = datetime.today()
            m_dob = datetime.strptime(postData["dob"], "%Y-%m-%d")    
            if m_dob > today:
                errors.append("Date of birth is not appropriate")
        if not EMAIL_REGEX.match(postData["email"]):
                errors.append("Invalid email address")      
        if len(User.objects.filter(email=postData["email"])) > 0:
            errors.append("Email already exist")
        if len(errors) > 0:
            return {"errors": errors}
        hp = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
        the_user = User.objects.create(first_name=postData["first_name"], last_name = postData["last_name"], email = postData["email"], dob=datetime.strptime(postData["dob"], "%Y-%m-%d"), password = hp)
        the_user.save()
        return {"the_user": the_user}

    def login(self, postData):
        errors = []
        try:
            the_user = User.objects.get(email = postData["email"])  
        except:
            errors.append("Email is invalid")
            return {"errors": errors}
        if bcrypt.checkpw(postData["password"].encode(), the_user.password.encode()):
            return {"the_user": the_user}
        else:
            errors.append("Wrong password")
            return {"errors": errors}


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class RecordManager(models.Manager):
    def add(self, postData, user_id):
        Record.objects.create(artist = postData["artist"],
        album = postData["album"],
        label = postData["label"],
        uploader = User.objects.get(id=user_id)
 


class Record(models.Model):
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, related_name="uploads")
    haters = models.ManyToManyField(User, related_name="hated_records")
    objects = RecordManager()
