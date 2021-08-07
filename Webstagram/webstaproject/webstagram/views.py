from django.shortcuts import render,redirect,get_object_or_404
from .models import Content
from django.contrib.auth.models import User

# Create your views here.

def feed(request,id):
    contents=get_object_or_404(Content,pk=id)
    return render(request,'feed.html',{'post':contents})

def profile(request,author_id):
    #모든 게시글 보여주기
    print('got author id')
    print(author_id)
    author=get_object_or_404(User,pk=author_id)
    author_posts=author.post.all()
    print("end of get all in profile url")
    return render(request,'profile.html',{'author':author,'posts':author_posts})

def edit(request,id):
    #edit 내에서 update 연결
    editpost=Content.objects.get(id=id)
    return render(request,'edit.html',{'post':editpost})

def new(request):
    #new.html 내에서 create 연결
    return render(request,'new.html')

def delete(request,id):
    #추가작업 없이 삭제
    this=Content.objects.get(id=id)
    this.delete()
    user=User.objects.get(username=request.user.username)
    return redirect('profile',author_id=user.id)

def update(request,id):
    #해당 글만 보여주는 걸로 바꾸기
    updatepost=Content.objects.get(id=id)
    updatepost.author=request.user
    updatepost.image=request.FILES['image']
    updatepost.save()
    
    user=User.objects.get(username=request.user.username)
 
    return redirect('profile',author_id=user.id)

def create(request):
    #나중에 해당 글 만 보여주는 걸로 바꾸기
    writepost=Content()
    writepost.author=request.user
    writepost.image=request.FILES['image']
    writepost.save()

    user=User.objects.get(username=request.user.username)
  
    return redirect('profile',author_id=user.id)
