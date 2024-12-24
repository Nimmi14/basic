from django import forms
from .models import Donar
from django.contrib.auth.forms import AuthenticationForm


class DonarForm(forms.ModelForm):
    class Meta:
        model = Donar
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Passwords do not match')


class DonarLoginForm(forms.Form):
    username= forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
# 'profile': forms.ClearableFileInput(attrs={'class': 'form-control'}),


class DonarProfileForm(forms.ModelForm):
    class Meta:
        model = Donar
        fields = ['username']