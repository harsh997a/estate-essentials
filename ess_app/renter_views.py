from django.shortcuts import render,redirect
from .models import Owner,Rented
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def renter_home(request):
    if request .method =="GET":
        return render(request,'ess_app/renter/renter_home.html')

def renter_login(request):
    if request .method =="GET":
        return render(request,'ess_app/renter/renter_login.html')
    if request.method=='POST':
        user_id=request.POST["userid"]
        password=request.POST["password"]
        print(user_id,password)
        list= Owner.objects.filter(owner_id=user_id,password=password,type='rented')
        print(list)
        l=len(list)
        if l>0:
            request.session["session_key"]=user_id #binding id to session
            request.session["role"]="renter"
            renter_object=Owner.objects.get(owner_id=user_id,type='rented')
            print("in renter",renter_object)
            context={
                "renter_data":renter_object
            }
            return render(request,'ess_app/renter/renter_home.html',context)
        else:
            messages.error(request,"invalid credentials")
            return render(request,'ess_app/renter/renter_login.html')
        


def renter_signout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("renter_login")

def rented_property(request):
    if request.method=='GET':
        owner_id=request.session["session_key"]
        context={
            "owner_id":owner_id
        }
        return render(request,'ess_app/renter/rented_property.html',context)

    if request.method=='POST':
        owner_id=request.session["session_key"]
        owner_property=request.POST["property"]
        price=request.POST["price"]
        facilities=request.POST["facilities"]
        city=request.POST["city"]
        address=request.POST["address"]
        contact=request.POST["contact"]
        pictures=request.FILES['pictures']
        fs=FileSystemStorage()
        file_obj=fs.save(pictures.name,pictures)
        print(file_obj)
        uploaded_file_url= fs.url(file_obj)
        print(uploaded_file_url)
        rented=Rented(user_id=owner_id,property_type=owner_property,rent_price=price,facilities=facilities,city=city,address=address,contact=contact,picture=pictures)
        rented.save()#to save data into contact table
        print("data saved")
        messages.success(request,"Thank you for Uploading")
        return render(request,'ess_app/renter/rented_property.html')


def renter_editprofile(request):
    if request .method =="GET":
        user_id=request.session["session_key"]
        renter_object=Owner.objects.get(owner_id=user_id)
        context={
            "renter_data":renter_object
        }
        return render(request,'ess_app/renter/renter_editprofile.html',context)
    
    if request.method=='POST':
        user_id=request.session["session_key"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        city=request.POST["city"]
        renter_object=Owner.objects.get(owner_id=user_id)
        renter_object.phone=phone
        renter_object.email=email
        renter_object.city=city
        renter_object.save()
        context={
                "renter_data":renter_object
            }
        return render(request,'ess_app/renter/renter_home.html',context)

def view_property(request):
    if request .method =="GET":
        user_id=request.session["session_key"]
        print(user_id)
        rentedlist=Rented.objects.filter(user_id=user_id)
        context={
            "rented_data":rentedlist
        }
        return render(request,'ess_app/renter/view_property.html',context)
    
def delete_rented(request,id):
    print(id)
    delete_obj=Rented.objects.get(id=id)
    user_id=request.session["session_key"]
    type=request.session["role"]
    renter_object=Owner.objects.get(owner_id=user_id,type='rented')
    print("in renter",renter_object)
    context={
        "renter_data":renter_object
        }
    #print(delete_obj.rent_price)
    delete_obj.delete()
    #print("property deleted",delete_obj)
    messages.success(request,"Details has been deleted")
    return render(request,'ess_app/renter/renter_home.html',context)


    