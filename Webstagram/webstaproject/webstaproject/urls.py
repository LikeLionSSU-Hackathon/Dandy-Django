"""webstaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webstagram import views as websta
from account import views as acc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',websta.home,name='home'),
    path('signIn/',acc.login_user,name='login'),
    path('logout/',acc.logout_user,name='logout'),
    path('signUp/',acc.signUp,name='signUp'),
    path('findEmail/',acc.find_email,name='findEmail'),
    path('findPwd/',acc.find_pwd,name='findPwd'),
    path('changePwd/<str:usermsg>',acc.changePwd,name='changePwd'),
    path('account/',websta.account,name='account'),
    path('mypage/',websta.mypage,name='mypage'),
    path('notice/',websta.notice,name='notice'),
    path('account/changePwd_account/<str:msg>',websta.changePwd_account,name='changePwd_account'),
    path('q1/',websta.q1,name='q1'),
    path('q2/',websta.q2,name='q2'),
    path('q3/',websta.q3,name='q3'),
    path('q4/',websta.q4,name='q4'),
    path('q5/',websta.q5,name='q5'),
    path('q6/',websta.q6,name='q6'),
    path('q7/',websta.q7,name='q7'),
    path('q8/',websta.q8,name='q8'),
    path('q8_1/',websta.q8_1,name='q8_1'),
    path('q9/',websta.q9,name='q9'),
    path('stylist/',websta.stylist,name='stylist'),
    path('matching/',websta.matching,name='matching'),
    path('stylistGuide/',websta.stylistGuide,name='stylistGuide'),
    path('userGuide/',websta.userGuide,name='userGuide'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
