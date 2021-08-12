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

def q1(request):
    return render(request,'question.html')

def q2(request):
    return render(request,'question2.html')

def q3(request):
    return render(request,'question3.html')

def q4(request):
    return render(request,'question4.html')

def q5(request):
    return render(request,'question5.html')

def q6(request):
    return render(request,'question6.html')

def q7(request):
    return render(request,'question7.html')

def q8_1(request):
    return render(request,'question8-1.html')

def q8(request):
    return render(request,'question8.html')

def q9(request):
    return render(request,'question9.html')

def stylist(request):
    return render(request,'stylist.html')

def matching(request):
    return render(request,'matching.html')

def stylistGuide(request):
    return render(request,'new_stylistguide.html')

def userGuide(request):
    return render(request,'new_userguide.html')


