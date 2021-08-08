from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm,RegisterForm
# Create your views here.

def login_user(request):
    if request.method == 'POST':
       print('method post in login')
       email=request.POST['email']
       password=request.POST['pwd']
       print('email: ',email,' pwd: ',password)

       form=LoginForm(request.POST)
       if form.is_valid():
            checkUser=User.objects.filter(email=email)
            if not checkUser.exists():
                print('user not exist')
                return render(request,'login.html',{'message':'login fail'})

            username=User.objects.get(email=email).username
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')  

            else:
                print('login fail')
                return render(request,'login.html',{'message':'login fail'})                

       else:
            print('form not valid')
            return render(request,'login.html',{'message':'empty value'})

    else:
        return render(request,'login.html')


    

def signUp(request):
    if request.method=='POST':
        print('method post in signup')
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['pwd']
        passwordCheck=request.POST['pwdCheck']
        phoneNum=request.POST['phoneNum']

        form=RegisterForm(request.POST)
        if not form.is_valid() :
            print('form not valid')
            return render(request,'signUp.html',{'message':'empty'})

        checkUser=User.objects.all().filter(email=email)
        if checkUser:
            print('user check: ',checkUser)
            return render(request,'signUp.html',{'message':'user exist'})
        

        if password!=passwordCheck:
            print('password 일치하지 않음')
            return render(request,'signUp.html',{'message':'password check fail'})
            #나중에 html로 값 보내고, js사용해서 html에서 받은 값으로 alert 띄우기

        user=User.objects.create_user(username=username,email=email,password=password)
        profile=Profile()
        profile.user=user
        profile.phoneNum=phoneNum
        profile.save()

        return render(request,'login.html',{'message':'join success'})
        
    else:
        return render(request,'signUp.html')



def logout_user(request):
    logout(request)
    return render(request,'login.html')

def find_email(request):
    #전화번호로 이메일 찾기
    #결과 보여주는 화면 연결


    #로그인 되어있는 상태에서 find email 하면 username이 현재 계정으로 2개 보내지는 문제 발생 => 로그인 되어있을 때는 사용 못하게 하자
    username=request.POST.get('find_username','')
    phoneNum=request.POST.get('phone','')
    checkUser=Profile.objects.filter(phoneNum=phoneNum)
    if not checkUser.exists():
        print('user not exist')
        return render(request,'findEmail.html',{'message':'user not exist'})
    else:
        name=Profile.objects.get(phoneNum=phoneNum).user.username
        print('name: ',name)
        if name==username:
            print('found user')
            return render(request,'findResult.html',{'message':Profile.objects.get(phoneNum=phoneNum).user.email})
        else:
            print('wrong phone number')
            return render(request,'findEmail.html',{'message':'user not exist'})


def find_pwd(request):
    #전화번호로 비밀번호 찾기
    #결과 보여주는 화면 연결
    #비밀번호 찾은 후, 2,3,4번쨰 글자느 *로 표시
    return render(request,'login.html')