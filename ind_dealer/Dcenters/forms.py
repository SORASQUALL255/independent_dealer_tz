from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import DealerCenter, Vehicle
from rest_framework import serializers



class DealerCenterForm(ModelForm):

    class Meta:
        model = DealerCenter
        exclude = ['dealer']


class VehicleForm(ModelForm):

    class Meta:
        model = Vehicle
        exclude = ['dealer']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))