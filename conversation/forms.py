from django import forms
from django.forms import Textarea

from .models import Messages


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={
                'rows': 2,
                'placeholder': 'Type something...'
            })
        }