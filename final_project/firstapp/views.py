from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import patient
from .models import Doctor


# Create your views here.

def form(request):
    
    if request.method == 'POST':
        p_id = request.POST['p_id']
        p_name = request.POST['p_name']
        disease_name = request.POST['disease_name']
        age = request.POST['age']
        sex = request.POST['sex']

        gk = patient(p_id=p_id,p_name=p_name,disease_name=disease_name,age=age,sex=sex)
        if gk:
            request.session['p_name'] = p_name
        gk.save()
        # print("hello")
        # return render(request, "confirmation.html")
        return redirect("/")
        
        
    return render(request, "form.html")
        # return redirect('/')    

def home(request):
    return render(request, "home.html", )

def home_2(request):
    return render(request, "home_2.html")

def home_3(request):
    return render(request, "home_3.html")

def register_doctor(request):
    if request.method == 'POST':
        d_id = request.POST['d_id']
        d_name = request.POST['d_name']
        qualifications = request.POST['qualifications']
        experience = request.POST['experience']
        Rating = request.POST['Rating']
        No_of_awards = request.POST['No_of_awards']

        grk = Doctor(d_id=d_id,d_name=d_name,qualifications=qualifications,experience=experience,Rating=Rating,No_of_awards=No_of_awards)
        grk.save()
        print("doctor register...")
        return render(request,"login.html")

    return render(request,"register_doctor.html")
    # return redirect('/')


def login(request):
    if request.method == 'POST':
        d_id = request.POST['d_id']
        d_name = request.POST['d_name']

        grk2 = Doctor.objects.filter(d_id=d_id, d_name=d_name).values()

        if grk2:
            request.session['d_id'] = d_id
            request.session['d_name'] = d_name
            # grk3 = grk2[0]
            
            print(grk2)
            # auth.login(request, grk2)
            return render(request,"home_3.html",{"grk2":grk2[0]})
        else:
            print("khoto avi gyo bhai...")
            messages.info(request, "su kars bhai???")
            return redirect('login')
    else:
        return render(request, "login.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,"home.html")
        else:
            messages.info(request, "invalid credentials")
            return redirect('signin')
    else:
        return render(request, "signin.html")



def register(request):


    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password == password2:
            if User.objects.filter(username=username).exists():
                # print('username taken')
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # print('email taken')
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created succesfully')
                return redirect('signin')
            
        else:
            messages.info(request,'password not matching..')
            return redirect('register')

        
        return redirect('/')



    else:
        return render(request, "register.html")
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def confirmation(request):
    return render(request, "feedback.html")

def view_appointment(request):
    if request.method == 'POST':
        amount = request.POST['set_amount']

        test = request.session['amount'] = amount
        print("hello..... bro.......")
        print(test)
        return render(request, "home.html", {"test":test})
    

    else:
        return render(request, "view_appointment.html")
    
    # return render(request, "home.html")

def feedback(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    phoneNumber = request.GET.get("phoneNumber")
    if name != None and email != None and phoneNumber != None:
        return render(request,"feedback.html",{"message":"Thank you for your feedback"})
    return render(request,"feedback.html",{"message":"None"})
    # return redirect("/")