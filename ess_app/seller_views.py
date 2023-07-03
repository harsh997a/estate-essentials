from django.shortcuts import render,redirect
from .models import Owner,Seller
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

def seller_home(request):
    if request .method =="GET":
        return render(request,'ess_app/seller/seller_home.html')

def seller_login(request):
    if request .method =="GET":
        return render(request,'ess_app/seller/seller_login.html')
    if request.method=='POST':
        user_id=request.POST["userid"]
        password=request.POST["password"]
        print(user_id,password)
        list= Owner.objects.filter(owner_id=user_id,password=password,type='seller')
        l=len(list)
        if l>0:
            request.session["session_key"]=user_id #binding id to session
            request.session["role"]="seller"
            seller_object=Owner.objects.get(owner_id=user_id,password=password,type='seller')
            context={
                "seller_data":seller_object
            }
            return render(request,'ess_app/seller/seller_home.html',context)
        else:
            messages.error(request,"invalid credentials")
            return render(request,'ess_app/seller/seller_login.html')
        

def seller_signout(request):
    del request.session["session_key"]
    del request.session["role"]
    return redirect("seller_login")

def seller_property(request):
    if request.method=='GET':
        owner_id=request.session["session_key"]
        context={
            "owner_id":owner_id
        }
        return render(request,'ess_app/seller/seller_property.html',context)

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
        seller=Seller(user_id=owner_id,property_type=owner_property,sell_price=price,facilities=facilities,city=city,address=address,contact=contact,picture=pictures)
        seller.save()#to save data into contact table
        print("data saved")
        messages.success(request,"Thank you for Adding Property Details")
        return render(request,'ess_app/seller/seller_property.html')
    
def seller_editprofile(request):
    if request .method =="GET":
        user_id=request.session["session_key"]
        seller_object=Owner.objects.get(owner_id=user_id)
        context={
            "seller_data":seller_object
        }
        return render(request,'ess_app/seller/seller_editprofile.html',context)
    
    if request.method=='POST':
        user_id=request.session["session_key"]
        phone=request.POST["phone"]
        email=request.POST["email"]
        city=request.POST["city"]
        seller_object=Owner.objects.get(owner_id=user_id)
        seller_object.phone=phone
        seller_object.email=email
        seller_object.city=city
        seller_object.save()
        context={
                "seller_data":seller_object
            }
        return render(request,'ess_app/seller/seller_home.html',context)
    
def property_view(request):
    if request .method =="GET":
        user_id=request.session["session_key"]
        print(user_id)
        sellerlist=Seller.objects.filter(user_id=user_id)
        context={
            "seller_data":sellerlist
        }
        return render(request,'ess_app/seller/property_view.html',context)
    
def delete_seller(request,id):
    print(id)
    delete_obj=Seller.objects.get(id=id)
    user_id=request.session["session_key"]
    type=request.session["role"]
    seller_object=Owner.objects.get(owner_id=user_id,type='seller')
    print("in seller",seller_object)
    context={
        "seller_data":seller_object
        }
    #print(delete_obj.rent_price)
    delete_obj.delete()
    #print("property deleted",delete_obj)
    messages.success(request,"Details has been deleted")
    return render(request,'ess_app/seller/seller_home.html',context)
    
  
    

    
