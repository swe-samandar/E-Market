
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['first_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser

        fields = ['first_name', 'email', 'job', 'bio', 'phone_number', 'tg_username', 'avatar']
        
# Bu UserCreationForm dan foydalanib qilingan forma, lekin men o'zim yozgan formadan foydalanib signupviewni yozdim
class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'username']