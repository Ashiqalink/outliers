# bot/forms.py
from django import forms
from .models import UserData
class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'interests', 'preferences']