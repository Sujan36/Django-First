from django.shortcuts import render
from django.http import *
from Sujan.models import *
from django.contrib.auth.hashers import make_password , check_password

# Create your views here.
def login_page(request):
    return render(request,'login.html')

def registerpage(req):
    return render(req,'register.html')

def submit(request):
    if(request.POST.get('email')):
        email =request.POST.get('email')
        password =request.POST.get('password')
        user_list = sujan_details.objects.values_list('email',flat=True)
        print(user_list)
        if email in user_list:
            user_details = sujan_details.objects.get(email=email)
            request.session['email'] = user_details.email
            
            if password == user_details.password:
                return HttpResponseRedirect('/homepage')
            else:
                return render(request,"login.html",{'error':'WRONG PASSWORD'})
        else:
            return render(request,"register.html",{'error':'EMAIL NOt found'})
        return HttpResponse()

def register(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    city = request.POST.get('city')
    qualification = request.POST.get('qualification')
    ambitions = request.POST.get('ambitions')
    hobbies = request.POST.get('hobbies')
    user_list = sujan_details.objects.values_list('email',flat=True)
    if email in user_list:
        return render(request,"login.html")
    else:
        if password == cpassword:
            password = make_password(password)
            sujan_details(name=name,email=email,password=password,city=city,qualification= qualification,ambitions=ambitions,hobbies=hobbies).save()

            return render(request,'login.html',{'msg':'Registration successfully completed'})
        else:
            return render(request,'register.html',{'error':'passwords are not matching'})


def homepage(req):
    email = req.session['email']
    print(email)
    user = sujan_details.objects.get(email=email)
    
    return render(req,'home.html',{'data':user})

def logout_user(request):
    logout(request)
    return render(reverse('login.html'))
