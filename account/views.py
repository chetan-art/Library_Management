
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from account.models import User
from account.backend import EmailBackEnd
from Home.views import Home
# Create your views here.
# This section is for signup for the new user

def Signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(email)
        if password != confirm_password:
            passnotmatch = True
            return render(request, "Signup.html", {'passnotmatch': passnotmatch})
        try:
            user = User.objects.create_superuser(email=email,name=name,mobile=mobile,password=password,confirm_password=confirm_password)
            user.save()
            return redirect('http://127.0.0.1:8000/Loginup')
        except:
            messages.error(request,"Email All ready register ")
            return render(request,"Signup.html")
    return render(request, "Signup.html")


def Loginup(request):
    if request.method == 'POST':
        useremail = request.POST['email']
        password = request.POST['password']
        user = EmailBackEnd.authenticate(request,email=useremail,password=password)
        if user != None:
            login(request, user)
            print(request.user.is_admin)
            if request.user.is_admin:
                return redirect('http://127.0.0.1:8000/Details/')
            else:
                messages.error(request,"You are not admin")
                return redirect('http://127.0.0.1:8000/Loginup')
        else:
            messages.info(request,"Username or Password is incorrect")
    return render(request,'Login.html')

def Studentregistration(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(email)
        if password != confirm_password:
            passnotmatch = True
            return render(request, "Student_Registration.html", {'passnotmatch': passnotmatch})
        try:
            user = User.objects.create_user(email=email,name=name,mobile=mobile,password=password,confirm_password=confirm_password)
            user.save()
            return redirect('http://127.0.0.1:8000/Student_Login')
        except:
            messages.error(request,"Email All ready register ")
            return render(request,"Student_Registration.html")
    return render(request, "Student_Registration.html")

def Student_Login(request):
    if request.method == 'POST':
        useremail = request.POST['email']
        password = request.POST['password']
        user = EmailBackEnd.authenticate(request,email=useremail,password=password)
        if user != None:
            login(request, user)
            print(request.user.is_active)
            if request.user.is_active:
                return redirect('http://127.0.0.1:8000/Details/')
            else:
                messages.error(request,"You are not student")
                return redirect('http://127.0.0.1:8000/Student_Login')
        else:
            messages.info(request,"Username or Password is incorrect")
    return render(request,'Student_Login.html')



# This is section for logout for the user
def LogoutPage(request):
    logout(request)
    # this is the redirect page where the user goes after the Logout
    return redirect('http://127.0.0.1:8000/')