from django.core import validators
from django import forms
from .models import user
class studentregisteration(forms.ModelForm):
    class Meta:
        model  = user
        fields=['name','email','password']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }