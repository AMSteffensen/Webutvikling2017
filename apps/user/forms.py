from django.contrib.auth.models import User
from django import forms
from .models import Profile
import re


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'Fornavn',
            'last_name': 'Etternavn',
            'email': 'Email',
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'date_of_birth', 'photo')
        labels = {
            'gender': 'Kjønn',
            'date_of_birth': 'Fødselsdato',
            'photo': 'Bilde',
        }
