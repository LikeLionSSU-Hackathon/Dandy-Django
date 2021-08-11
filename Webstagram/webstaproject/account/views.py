from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm,RegisterForm
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == 'POST':
       next=request.POST.get('next','/')
       email=request.POST['email']
       password=request.POST['pwd']

       form=LoginForm(request.POST)
       if form.is_valid():
            checkUser=User.objects.filter(email=email)
            if not checkUser.exists():
                print('user not exist')
                messages.error(request,'존재하지 않는 계정입니다. 이메일 또는 비밀번호를 다시 확인해주세요.')
                return HttpResponseRedirect(next)

            username=User.objects.get(email=email).username
            user=authenticate(username=username,password=password)
            if user is not None:
                #여기서 이메일도 비교 (get한 user의 email과 입력 email 비교해서 맞으면 login, 아니면 다른 user 찾기? )
                login(request,user)
                return redirect('home')  

            else:
                print('login fail')
                messages.error(request,'존재하지 않는 계정입니다. 이메일 또는 비밀번호를 다시 확인해주세요.')
                return HttpResponseRedirect(next)              

       else:
            print('form not valid')
            return render(request,'login.html',{'message':'empty value'})

    else:
        return render(request,'login.html')


    

def signUp(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['pwd']
        passwordCheck=request.POST['pwdCheck']
        phoneNum=request.POST['phoneNum']
        next=request.POST.get('next','/')

        form=RegisterForm(request.POST)
        if not form.is_valid() :
            print('form not valid')
            return render(request,'signUp.html',{'message':'empty'})

        checkUser=User.objects.all().filter(email=email)
        if checkUser:
            #print('user check: ',checkUser)
            messages.error(request,'이미 가입되어 있는 이메일 입니다.')
            return HttpResponseRedirect(next)
            #return render(request,'signUp.html',{'message':'user exist'})
        

        if password!=passwordCheck:
            print('password 일치하지 않음')
            messages.error(request,'비밀번호를 다시 한 번 확인해주세요.')
            return HttpResponseRedirect(next)

        user=User.objects.create_user(username=username,email=email,password=password)
        profile=Profile()
        profile.user=user
        profile.phoneNum=phoneNum
        profile.save()

        #messages.success(request,'회원가입 성공!')
        #return HttpResponseRedirect('login')
        return render(request,'login.html',{'message':'join success'})
        
    else:
        return render(request,'signUp.html')



def logout_user(request):
    logout(request)
    return redirect('home')


def find_email(request):
    #전화번호로 이메일 찾기
    #결과 보여주는 화면 연결
  if request.method=='POST':
    username=request.POST.get('find_username','')
    phoneNum=request.POST.get('phone','')
    next=request.POST.get('next','/')

    checkUser=Profile.objects.filter(phoneNum=phoneNum)
    if not checkUser.exists():
        print('phone number user not exist')
        messages.error(request,'회원정보를 다시 한 번 확인해주세요.')
        return HttpResponseRedirect(next)
    else:
        name=Profile.objects.get(phoneNum=phoneNum).user.username
        #print('name: ',name)
        if name==username:
            print('found user')
            return render(request,'findResult.html',{'message':Profile.objects.get(phoneNum=phoneNum).user.email})
        else:
            print('username and phone number match fail')
            messages.error(request,'회원정보를 다시 한 번 확인해주세요.')
            return HttpResponseRedirect(next)

  else:
      return render(request,'findEmail.html')


def find_pwd(request):
    #전화번호로 비밀번호 찾기
    #결과 보여주는 화면 연결
  if request.method=='POST':
    username=request.POST.get('find_username','')
    phoneNum=request.POST.get('phone','')
    email=request.POST.get('email','')
    next=request.POST.get('next','/')

    checkUser=Profile.objects.filter(phoneNum=phoneNum)
    if not checkUser.exists():
        print('user not exist by phone number')
        messages.error(request,'회원정보를 다시 한 번 확인해주세요.')
        return HttpResponseRedirect(next)
    else:
        findUser=Profile.objects.get(phoneNum=phoneNum).user
        print('found user: ',findUser)
        if findUser.username==username and findUser.email==email:
            print('found user')
            return render(request,'changePwd.html',{'usermsg':findUser.email})
        else:
            print('wrong email or name')
            messages.error(request,'회원정보를 다시 한 번 확인해주세요.')
            return HttpResponseRedirect(next)

  else:
      return render(request,'findPassword.html')

    
    #비밀번호 찾은 후, 2,3,4번쨰 글자느 *로 표시

def changePwd(request,usermsg):
  if request.method=='POST':
    newPw=request.POST.get('pwd','')
    pwCheck=request.POST.get('pwdCheck','')
    next=request.POST.get('next','/')

    if(newPw!=pwCheck):
        print('password check fail')
        #messages.error(request,'비밀번호가 일치하지 않습니다.')
        #return HttpResponseRedirect(next)
        return render(request,'changePwd.html',{'message':'비밀번호가 일치하지 않습니다. ','usermsg':usermsg})

    user=User.objects.get(email=usermsg)
    user.set_password(newPw)
    #print(newPw)
    user.save()
    return redirect('login')
  else:
      return render(request,'changePwd.html',{'message':' ','usermsg':usermsg})


