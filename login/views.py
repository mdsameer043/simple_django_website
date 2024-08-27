from django.shortcuts import render
from datetime import datetime
from login.models import logindata


def signup(request):
    context={
        'invalid':"invalid"
    }
    if request.method=="POST" and request.POST.get('signinValidation')=="signin":
        email=request.POST.get('signinEmail')
        password=request.POST.get('signinPassword')
        confirmPassword=request.POST.get('signinConfirmPassword')
        if len(email) and len(password) !=0:
            if password==confirmPassword:
                details=logindata(email=email,password=password,date=datetime.today())
                details.save()
            else:
                return render(request,'signin.html',context)
        else:
            return render(request,'signin.html')
        
    elif request.method=="POST" and request.POST.get('signupValidation')=="signup":
        context={
            'invalid':"invalid",
            'logout':"logout"
        }
        db=logindata.objects.all()
        jobs={}
        for items in db:
            jobs[items.email]=items.password
            
        email=request.POST.get('signupEmail')
        password=request.POST.get('signupPassword')
        if jobs.get(email)==password:
            return render(request,'index.html',context)
        else:
            return render(request,'signup.html',context)
                        
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')
# Create your views here.

