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
    path('',acc.login_user,name='login'),
    path('feed/<str:id>',websta.feed,name='feed'),
    path('edit/<str:id>',websta.edit,name='edit'),
    path('delete/<str:id>',websta.delete,name='delete'),
    path('create/',websta.create,name='create'),
    path('new/',websta.new,name='new'),
    path('update/<str:id>',websta.update,name='update'),
    path('profile/<int:author_id>',websta.profile,name='profile'),
    path('logout/',acc.logout_user,name='logout'),
    path('signUp/',acc.signUp,name='signUp'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
