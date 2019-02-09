from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import User1


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    contact_Number_1 = forms.CharField(max_length=10)

    class Meta:
        model = User1
        fields = ['username', 'email','contact_Number_1', 'password1', 'password2']
