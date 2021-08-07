from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.
def login_user(request):
    if request.method == 'POST':
       print('method post in login')
       username=request.POST['username']
       password=request.POST['pwd']
       user=authenticate(username=username,password=password)
       if user is not None:
           #login 가능
           login(request,user)
           print("user id: ")
           print(user.id)
           return redirect('profile',author_id=user.id)
    else:
        return render(request,'login.html')
    

def signUp(request):
    if request.method=='POST':
        print('method post in signup')
        email=request.POST['email']
        realname=request.POST['realname']
        username=request.POST['username']
        password=request.POST['pwd']
        new_user=User.objects.create_user(email=email,username=username,password=password)
        new_user.save()
        login(request,new_user)
        return redirect('profile',author_id=new_user.id)
        
    else:
        return render(request,'signUp.html')



def logout_user(request):
    logout(request)
    return render(request,'login.html')