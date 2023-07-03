from django.shortcuts import render
from .models import user_Message
from django.contrib import messages
from django.http import JsonResponse


def compose(request):
    if request.method=='GET':
        user_role=request.session['role']# to fetch value from session
        sender_id=request.session["session_key"]
        context={"sender_id":sender_id}
        if user_role=='vastu':
            return render(request,'ess_app/vastu/vastu_compose.html',context)
        if user_role=='seller':
            return render(request,'ess_app/seller/seller_compose.html',context)
        if user_role=='renter':
            return render(request,'ess_app/renter/renter_compose.html',context)
        if user_role=='client':
            return render(request,'ess_app/client/client_compose.html',context)
        

    if request.method=='POST':
        sender_id=request.session["session_key"]
        receiver_status=True
        sender_status=True
        receiver_id=request.POST["receiver"]
        subject=request.POST["subject"]
        content=request.POST["content"]
        user_message=user_Message(sender_id=sender_id,receiver_status=True,sender_status=True,subject=subject,content=content,receiver_id=receiver_id)
        user_message.save()
        user_role=request.session['role']
        messages.success(request,"Message has been sent successfullly")
        if user_role=='vastu':
            return render(request,'ess_app/vastu/vastu_compose.html',)
        if user_role=='seller':
            return render(request,'ess_app/seller/seller_compose.html')
        if user_role=='renter':
            return render(request,'ess_app/renter/renter_compose.html')
        if user_role=='client':
            return render(request,'ess_app/client/client_compose.html')
        


def inbox(request):
    if request.method=='GET':
        user_role=request.session['role']# to fetch value from session
        receiver_id=request.session["session_key"]
        message_object_list=user_Message.objects.filter(receiver_id=receiver_id,receiver_status=True)
        context={"message_object":message_object_list}
        if user_role=='vastu':
            return render(request,'ess_app/vastu/vastu_inbox.html',context)
        if user_role=='seller':
            return render(request,'ess_app/seller/seller_inbox.html',context)
        if user_role=='renter':
            return render(request,'ess_app/renter/renter_inbox.html',context)
        if user_role=='client':
            return render(request,'ess_app/client/client_inbox.html',context)
        

def sentItem(request):
    if request.method=='GET':
        user_role=request.session['role']# to fetch value from session
        sender_id=request.session["session_key"]
        message_object_list=user_Message.objects.filter(sender_id=sender_id,sender_status=True)
        context={"message_object":message_object_list}
        if user_role=='vastu':
            return render(request,'ess_app/vastu/vastu_sentitem.html',context)
        if user_role=='seller':
            return render(request,'ess_app/seller/seller_sentitem.html',context)
        if user_role=='renter':
            return render(request,'ess_app/renter/renter_sentitem.html',context)
        if user_role=='client':
            return render(request,'ess_app/client/client_sentitem.html',context)


def validate_ip_username(request):
    username=request.GET['username']
    context={
        'exists':user_Message.objects.filter(receiver_id__iexact=username).exists()
    }
    return JsonResponse(context) 


def delete_message(request):
    if request.method=='POST':
        receiver_id=request.session["session_key"]
        user_role=request.session['role']# to fetch value from session
        message_id_list=request.POST.getlist("checkid")
        # print(message_id_list)
        for mid in message_id_list:
            message_object=user_Message.objects.get(id=mid)
            message_object.receiver_status=False
            message_object.save()
        message_object_list=user_Message.objects.filter(receiver_id=receiver_id,receiver_status=True)
        context={"message_object":message_object_list}
        if user_role=='vastu':
            return render(request,'ess_app/vastu/vastu_inbox.html',context)
        if user_role=='seller':
            return render(request,'ess_app/seller/seller_inbox.html',context)
        if user_role=='renter':
            return render(request,'ess_app/renter/renter_inbox.html',context)
        if user_role=='client':
            return render(request,'ess_app/client/client_inbox.html',context)
        



def delete_sentitem(request):
    if request.method=='POST':
        sender_id=request.session["session_key"]
        user_role=request.session['role']# to fetch value from session
        message_id_list=request.POST.getlist("checkid")
        # print(message_id_list)
        for mid in message_id_list:
            message_object=user_Message.objects.get(id=mid)
            message_object.sender_status=False
            message_object.save()
        message_object_list=user_Message.objects.filter(sender_id=sender_id,sender_status=True)
        context={"message_object":message_object_list}
        if user_role=='vastu':
            return render(request,'ess_app/vastu/vastu_sentitem.html',context)
        if user_role=='seller':
            return render(request,'ess_app/seller/seller_sentitem.html',context)
        if user_role=='renter':
            return render(request,'ess_app/renter/renter_sentitem.html',context)
        if user_role=='client':
            return render(request,'ess_app/client/client_sentitem.html',context)
        

        


