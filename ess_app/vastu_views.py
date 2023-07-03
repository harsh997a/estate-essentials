from django.shortcuts import render,redirect
from .models import Consultant,Tips
from django.contrib import messages
from django.http import JsonResponse

def vastu_home(request):
    if request .method =="GET":
        return render(request,'ess_app/vastu/vastu_home.html')


def vastu_login(request):
    if request .method =="GET":
        return render(request,'ess_app/vastu/vastu_login.html')
    if request.method=='POST':
        user_id=request.POST["userid"]
        password=request.POST["userpassword"]
        print(user_id,password)
        list= Consultant.objects.filter(user_id=user_id,password=password)
        l=len(list)
        if l>0:
            request.session["session_key"]=user_id #binding id to session
            request.session["role"]="vastu"
            vastu_object=Consultant.objects.get(user_id=user_id)
            context={
                "vastu_data":vastu_object
            }
            return render(request,'ess_app/vastu/vastu_home.html',context)
        else:
            messages.error(request,"invalid credentials")
            return render(request,'ess_app/vastu/vastu_login.html')
        
        

        

def consultant_registration(request):
    if request .method =="GET":
        return render(request,'ess_app/vastu/consultant_registration.html')
    
    if request.method=='POST':
        user_id=request.POST["userid"]
        user_password=request.POST["password"]
        user_name=request.POST["username"]#request.post is a dict and control name(textbox ,select,radio) is the key
        user_email=request.POST["useremail"]
        user_phone=request.POST["userphone"]
        user_address=request.POST["address"]
        experience=request.POST["experience"]
        consult=Consultant(user_id=user_id,password=user_password,name=user_name,email=user_email,phone=user_phone,address=user_address,experience=experience)
        consult.save()#to save data into contact table
        print("data saved")
        messages.success(request,"Thank you for Registration")
        return render(request,'ess_app/vastu/consultant_registration.html')
   
def tips(request):
    if request .method =="GET":
        return render(request,'ess_app/vastu/tips.html')
    if request.method=='POST':
        user_id= request.session["session_key"]
        consultant=Consultant.objects.get(user_id=user_id)
        vname=consultant.name
        #consultantid=request.POST["consultantid"]
        consultanttips=request.POST["tips"]
        tips=Tips(consultant_id=vname,tips_content=consultanttips)
        tips.save()#to save data into contact table
        print("data saved")
        messages.success(request,"Thank you for giving tips.")
        return render(request,'ess_app/vastu/tips.html')
    

def vastu_signout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("vastu_login")

def vastu_editprofile(request):
    if request .method =="GET":
        user_id=request.session["session_key"]
        vastu_object=Consultant.objects.get(user_id=user_id)
        context={
            "vastu_data":vastu_object
        }
        return render(request,'ess_app/vastu/vastu_editprofile.html',context)
    
    if request.method=='POST':
        user_id=request.session["session_key"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        address=request.POST["address"]
        experience=request.POST["experience"]
        vastu_object=Consultant.objects.get(user_id=user_id)
        vastu_object.phone=phone
        vastu_object.email=email
        vastu_object.address=address
        vastu_object.experience=experience
        vastu_object.save()
        context={
                "vastu_data":vastu_object
            }
        return render(request,'ess_app/vastu/vastu_home.html',context)
    

def validate_ip_username(request):
    username=request.GET['username']
    context={
        'exists':Consultant.objects.filter(user_id__iexact=username).exists()
    }
    return JsonResponse(context) 
    
  
    

    


    
    
