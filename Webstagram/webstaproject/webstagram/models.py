from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Content(models.Model): 
    image=models.ImageField(upload_to='webimg/',blank=True,null=True)
    author=models.ForeignKey(User,related_name="post",on_delete=CASCADE)
