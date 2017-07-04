from django.contrib.auth.models import User
from django import forms
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Brukernavn / Email', required=True, error_messages={'required': 'Vennligst fyll in dette feltet'})
    password = forms.CharField(label='Passord', widget=forms.PasswordInput, required=True)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Passord', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Gjenta Passord', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        labels = {
            'username': 'Brukernavn',
            'first_name': 'Fornavn',
            'email': 'Email',
        }


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].require = True
        self.fields['username'].error_messages={'required': 'Vennligst fyll in dette feltet'}
        self.fields['first_name'].require = True
        self.fields['email'].require = True


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


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