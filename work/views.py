from pyexpat import model
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import user

# Create your views here[


def home(request):
    print('hai adhin')
    return render(request,'signup.html')
def rooms(request,pk):
    name=request.GET['username']
    email1=request.GET['email']
    password=request.GET['password']
    print(name)
    print(email1)
    print(password)
    data= user(name=name,email=email1,password=password) 
    if data!=None:
        # data.save()
        print("data save ayee")
    



    users=user.objects.all()
    print("aldjfaldfjalsdf")
    
    
  
 
    # for i in data:
    #   if int(pk)==i['id']:
    #     print("kkkkkkkkkkkkkkkk")
    #     val=i
    #     con={"val":val}
    #     print(con["val"])
    
    
    return render(request,'room.html',{"data":users})


def delete(request,pk):
    print(pk)
    
    record=user.objects.filter(id=pk)
    record.delete()
    print("data deleted")
   
    # return render (request,'room.html')
    return redirect(request.META['HTTP_REFERER'])
    
