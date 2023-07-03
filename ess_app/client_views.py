from django.shortcuts import render,redirect
from .models import Client
from django.contrib import messages
from django.http import JsonResponse

    
def client_home(request):
    if request .method =="GET":
        return render(request,'ess_app/client/client_home.html')
    
def client_login(request):
    if request .method =="GET":
        return render(request,'ess_app/client/client_login.html')
    if request.method=='POST':
        user_id=request.POST["userid"]
        password=request.POST["password"]
        print(user_id,password)
        list= Client.objects.filter(client_id=user_id,password=password)
        l=len(list)
        if l>0:
            request.session["session_key"]=user_id #binding id to session
            request.session["role"]="client"
            client_object=Client.objects.get(client_id=user_id,password=password)
            context={
                "client_data":client_object
            }
            return render(request,'ess_app/client/client_home.html',context)
        else:
            messages.error(request,"invalid credentials")
            return render(request,'ess_app/client/client_login.html')



def client_registration(request):
    if request .method =="GET":
        return render(request,'ess_app/client/client_registration.html')
    
    if request.method=='POST':
        client_id=request.POST["clientid"]
        password=request.POST["password"]
        name=request.POST["name"]#request.post is a dict and control name(textbox ,select,radio) is the key
        email=request.POST["email"]
        phone=request.POST["phone"]
        client=Client(client_id=client_id,password=password,name=name,email=email,phone=phone)
        client.save()#to save data into contact table
        print("data saved")
        messages.success(request,"Thank you for Registration")
        return render(request,'ess_app/client/client_registration.html')

    
def client_signout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("client_login")

def client_editprofile(request):
    if request .method =="GET":
        user_id=request.session["session_key"]
        client_object=Client.objects.get(client_id=user_id)
        context={
            "client_data":client_object
        }
        return render(request,'ess_app/client/client_editprofile.html',context)
    
    if request.method=='POST':
        user_id=request.session["session_key"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        # city=request.POST["city"]
        client_object=Client.objects.get(client_id=user_id)
        client_object.phone=phone
        client_object.email=email
        # client_object.city=city
        client_object.save()
        context={
                "client_data":client_object
            }
        return render(request,'ess_app/client/client_home.html',context)
    
def validate_ip_username(request):
    username=request.GET['username']
    context={
        'exists':Client.objects.filter(client_id__iexact=username).exists()
    }
    return JsonResponse(context) 
    
    
  