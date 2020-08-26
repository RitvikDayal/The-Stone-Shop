from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name'}),required = True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),required = True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),required = True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
