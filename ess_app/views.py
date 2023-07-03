from django.shortcuts import render,HttpResponse
from .models import Scheme,Query,Feedback_Rating,Owner,Rented,Seller,Tips
from django.contrib import messages
from django.http import JsonResponse
import pandas as pd
import pickle


# Create your views here.
def home(request):
    scheme_list=Scheme.objects.all() #it is used to fetch all objects from table
    tips_list=Tips.objects.all()
    # print(scheme_list)
    scheme_dict={
        "scheme_key":scheme_list,
        "tips_key":tips_list
        }
    return render(request,'ess_app/html/index.html',scheme_dict)#passing the dictonary on the html page



def contactus(request):
    if request.method=='GET':
        return render(request,'ess_app/html/contactus.html')
    
    if request.method=='POST':
        user_name=request.POST["name"]#request.post is a dict and control name(textbox ,select,radio) is the key
        user_email=request.POST["email"]
        user_phone=request.POST["phone"]
        user_query=request.POST["query"]
        query=Query(name=user_name,email=user_email,phone=user_phone,user_query=user_query) #creating objects
        query.save()#to save data into contact table
        print("data saved")
        messages.success(request,"Thank you for contacting us we will reach you soon")
        return render(request,'ess_app/html/contactus.html')
        


def aboutus(request):
    return render(request,'ess_app/html/aboutus.html')



def feedback(request):
    if request.method=='GET':
        return render(request,'ess_app/html/feedback.html')
    
    if request.method=='POST':
        user_name=request.POST["name"]#request.post is a dict and control name(textbox ,select,radio) is the key
        user_email=request.POST["email"]
        user_phone=request.POST["phone"]
        user_feedback=request.POST["feedback"]
        user_ratings=request.POST["rate"]
        feed=Feedback_Rating(name=user_name,email=user_email,phone=user_phone,feedback_text=user_feedback,rating=user_ratings) #creating objects
        feed.save()#to save data into contact table
        print("data saved")
        messages.success(request,"Thank you for your feedback")
        return render(request,'ess_app/html/feedback.html')
    

def owner_registration(request):
    if request .method =="GET":
        return render(request,'ess_app/html/owner_registration.html')
    
    if request.method=='POST':
        owner_id=request.POST["ownerid"]
        user_password=request.POST["password"]
        user_name=request.POST["username"]#request.post is a dict and control name(textbox ,select,radio) is the key
        user_email=request.POST["useremail"]
        user_phone=request.POST["userphone"]
        user_city=request.POST["city"]
        user_address=request.POST["address"]
        user_type=request.POST["type"]
        own=Owner(owner_id=owner_id,password=user_password,name=user_name,email=user_email,phone=user_phone,city=user_city,address=user_address,type=user_type)
        own.save()#to save data into contact table
        print("data saved")
        # messages.success(request,"Thank you for Registration")
        return render(request,'ess_app/html/owner_registration.html')
    
def rented_view(request):
    if request .method =="GET":
        rentedlist=Rented.objects.all()
        context={
                "rented_data":rentedlist
            }
        return render(request,'ess_app/html/rented_view.html',context)
    
    
def seller_view(request):
    if request .method =="GET":
        sellerlist=Seller.objects.all()
        context={
                "seller_data":sellerlist
            }
        return render(request,'ess_app/html/seller_view.html',context)
    

def citywise_rentedhouse(request):
    if request.method=='GET':
        return render(request,'ess_app/html/citywise_rentedhouse.html')

    if request.method=='POST':
        cityname=request.POST["cityname"]
        property_list=Rented.objects.filter(city=cityname)
        print(cityname)
        context={
            "citywise_data":property_list
        }
        
        return render(request,'ess_app/html/specific_cityrentedhouse.html',context)
    




def citywise_property(request):
    if request.method=='GET':
        return render(request,'ess_app/html/citywise_property.html')

    if request.method=='POST':
        cityname=request.POST["cityname"]
        property_list=Seller.objects.filter(city=cityname)
        print(cityname)
        context={
            "citywise_data":property_list
        }
        
        return render(request,'ess_app/html/specific_cityproperty.html',context)
    

def validate_ip_username(request):
    username=request.GET['username']
    context={
        'exists':Owner.objects.filter(owner_id__iexact=username).exists()
    }
    return JsonResponse(context)  

def viewcontent(request,id):
    # print(id)
    scheme_obj=Scheme.objects.get(id=id)
    context={"scheme_data":scheme_obj}
    return render(request,'ess_app/html/viewcontent.html',context)



def ml_predict(request):
      if request.method=="GET":
            data= pd.read_csv("data.csv")
            locations=sorted(data['location'].unique())
            square_feet=sorted(data['total_squarefeet'].unique())
            bath_room=sorted(data['bathroom'].unique())
            flat_type=sorted(data['size'].unique())
            print(flat_type)
            context={

                  "loc":locations,
                  "sq":square_feet,
                  "br":bath_room,
                  "flat_type":flat_type
            }
            return render(request,'ess_app/html/priceprediction.html',context)
      if request.method=="POST":
           
            #pipe=joblib.load('realEstate.joblib'
            data= pd.read_csv("data.csv")
            locations=sorted(data['location'].unique())
            square_feet=sorted(data['total_squarefeet'].unique())
            bath_room=sorted(data['bathroom'].unique())
            flat_type=sorted(data['size'].unique())
            file_data=pickle.load(open('realEstate.pkl','rb'))
            (file_data)
            location=request.POST["location"]#request.POST is a dict and control name(textbox,select,radio) is the key
            bhk=request.POST["bhk"]
            bath=request.POST["bath"]
            sqft=request.POST['square_feet']
            print(location,bhk,bath,sqft)
            input=pd.DataFrame([[location,bhk,sqft,bath]],columns=['location','size','total_squarefeet','bathroom'])
            print(input)
            predicted_price= file_data.predict(input)[0]
            print("predicted price is ",predicted_price)
            context={

                  "price":predicted_price,
                  "loc":locations,
                  "sq":square_feet,
                  "br":bath_room,
                  "flat_type":flat_type
            }
            messages.success(request, f"According to given data the predicted price is ₹‚ {predicted_price}  ")
      return render(request,'ess_app/html/priceprediction.html',context)





 
    

    



    

