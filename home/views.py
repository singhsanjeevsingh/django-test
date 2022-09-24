import email
from django.shortcuts import render,HttpResponse
from home.models import student_details
from django.contrib import messages
from django.db.models import Q


# Create your views here.

def register(request):
    if request.method=="POST":
        fname= request.POST.get('firstname')
        mname= request.POST.get('middlename')
        lname= request.POST.get('lastname')
        course= request.POST.get('course')
        gender= request.POST.get('gender')
        phone= request.POST.get('phone')
        curadd= request.POST.get('curadd')
        email= request.POST.get('email')
        psw= request.POST.get('psw')
        psw_repeat= request.POST.get('psw_repeat')

        details = student_details(fname=fname,
                                  lname=lname,
                                  mname=mname,
                                  course=course,
                                  gender=gender,
                                  phone=phone,
                                  curadd=curadd,
                                  email=email,
                                  paswd=psw)
        if psw==psw_repeat and fname != "":
            details.save()
            messages.success(request, 'Registered Sucessfully')   
            return render(request,"login.html")
        else:
            messages.warning(request, 'check your password')   
            return render(request,"register.html")    
    return render(request,"register.html")
def login(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        result = student_details.objects.filter(Q(email=email) & Q(paswd=password))
    
        if len(result)>0:
            return render(request,"home.html")
        else:
            messages.warning(request, 'wrong credentals')   
            return render(request,"login.html")
    return render(request,"login.html")

def home(request):
    return render(request,"login.html")