from django import forms
class LoginForm(forms.Form):
    email=forms.CharField(min_length=1,max_length=20)
    pwd=forms.CharField(min_length=1,max_length=20)

class RegisterForm(forms.Form):
    email=forms.CharField(min_length=1,max_length=20)
    pwd=forms.CharField(min_length=1,max_length=20)
    username=forms.CharField(min_length=1,max_length=10)
    phoneNum=forms.CharField(min_length=1,max_length=20)