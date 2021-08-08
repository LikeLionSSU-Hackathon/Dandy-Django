from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(models.Model): 
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=200)
    phoneNum=models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE)
    phoneNum=models.CharField(max_length=20,blank=True)



