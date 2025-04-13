from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", 'email', "tg_username", 'phone_number', 'avatar')