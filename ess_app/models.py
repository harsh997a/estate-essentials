from django.db import models
from django.utils import timezone

# Create your models here.
class Scheme(models.Model):
    scheme_topic=models.CharField(max_length=45,null=False)
    scheme_contents=models.CharField(max_length=100,null=False)
    date=models.DateField(default=timezone.now)
   

class Query(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10,null=False)
    user_query=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Feedback_Rating(models.Model):
    name=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=45,null=False)
    phone=models.CharField(max_length=10,null=False)
    feedback_text=models.TextField()
    rating=models.CharField(max_length=6,null=False)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name


class user_Message(models.Model):
    receiver_id=models.CharField(max_length=45,default=None,null=False)
    sender_id=models.CharField(max_length=45,default=None,null=False)
    subject=models.CharField(max_length=100,default=None,null=False)
    content=models.TextField(null=False)
    date=models.DateField(default=timezone.now)
    receiver_status=models.BooleanField(default=True,null=True)
    sender_status=models.BooleanField(default=True,null=True)

class Tips(models.Model):
    consultant_id=models.CharField(max_length=45,default=None,null=False)
    tips_content=models.TextField(null=False)
    date=models.DateField(default=timezone.now)

class Consultant(models.Model):
    user_id=models.CharField(max_length=45,default=None,null=False,primary_key=True)
    password=models.CharField(max_length=45,default=None,null=False)
    name=models.CharField(max_length=100,default=None,null=False)
    email=models.CharField(max_length=100,default=None,null=False)
    phone=models.CharField(max_length=100,default=None,null=False)
    address=models.TextField(null=False)
    experience=models.CharField(max_length=100,default=None,null=False)
    date=models.DateField(default=timezone.now)

class Owner(models.Model):
    owner_id=models.CharField(max_length=45,default=None,null=False,primary_key=True)
    password=models.CharField(max_length=45,default=None,null=False)
    name=models.CharField(max_length=100,default=None,null=False)
    email=models.CharField(max_length=100,default=None,null=False)
    phone=models.CharField(max_length=100,default=None,null=False)
    city=models.CharField(max_length=100,default=None,null=False)
    address=models.TextField(null=False)
    type=models.CharField(max_length=100,default=None,null=False)
    date=models.DateField(default=timezone.now)

class Client(models.Model):
    client_id=models.CharField(max_length=45,default=None,null=False,primary_key=True)
    password=models.CharField(max_length=45,default=None,null=False)
    name=models.CharField(max_length=100,default=None,null=False)
    email=models.CharField(max_length=100,default=None,null=False)
    phone=models.CharField(max_length=100,default=None,null=False)


class Rented(models.Model):
    user_id=models.CharField(max_length=45,default=None,null=False)
    property_type=models.CharField(max_length=45,default=None,null=False)
    rent_price=models.CharField(max_length=100,default=None,null=False)
    facilities=models.TextField(null=False)
    city=models.CharField(max_length=100,default=None,null=False)
    address=models.TextField(null=False)
    contact=models.CharField(max_length=100,default=None,null=False)    
    picture=models.FileField(max_length=100,upload_to="ess_app/photo",default="")
    date=models.DateField(default=timezone.now)


class Seller(models.Model):
    user_id=models.CharField(max_length=45,default=None,null=False)
    property_type=models.CharField(max_length=45,default=None,null=False)
    sell_price=models.CharField(max_length=100,default=None,null=False)
    facilities=models.TextField(null=False)
    city=models.CharField(max_length=100,default=None,null=False)
    address=models.TextField(null=False)
    contact=models.CharField(max_length=100,default=None,null=False)    
    picture=models.FileField(max_length=100,upload_to="ess_app/photo",default="")
    date=models.DateField(default=timezone.now)