from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request,'home.html')


#우선은 로그인되어있는 사람 / 아닌사람 식별해서 보여주게만 만들어놨습니다
def account(request):
    cur_user=request.user
    print('cur user: ',cur_user)
    if cur_user.is_authenticated:
        account=Profile.objects.get(user=cur_user)
        return render(request,'account.html',{'user_profile':account})
    else:
        return redirect('login')

def mypage(request):
    cur_user=request.user
    print('cur user: ',cur_user)
    if cur_user.is_authenticated:
        account=User.objects.get(email=cur_user.email)
        return render(request,'mypage.html',{'user':account})
    else:
        return redirect('login')

def notice(request):
    return render(request,'notice.html')


def changePwd_account(request,msg):
    if request.method=='POST':
        newPw=request.POST.get('pwd','')
        pwCheck=request.POST.get('pwdCheck','')
        next=request.POST.get('next','/')

        if(newPw!=pwCheck):
            print('password check fail')
            #messages.error(request,'비밀번호가 일치하지 않습니다.')
            #return HttpResponseRedirect(next)
            return render(request,'changePwd.html',{'message':'비밀번호가 일치하지 않습니다. ','usermsg':msg})

        user=User.objects.get(email=msg)
        user.set_password(newPw)
        #print(newPw)
        user.save()
        return redirect('login')
    else:
        print('msg from account: ',msg)
        return render(request,'changePwd.html',{'message':' ','usermsg':msg})