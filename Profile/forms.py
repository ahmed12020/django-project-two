from django import forms
from .models import Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'body']


class SignForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email' , 'first_name', 'last_name', 'password1', 'password2']