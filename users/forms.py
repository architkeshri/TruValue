from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import models
from .models import profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name=forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1','password2']

class UserUpdateForm(models.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields=['username','email']
class ProfileUpdateForm(models.ModelForm):
    class Meta:
        model= profile
        fields=['image']
