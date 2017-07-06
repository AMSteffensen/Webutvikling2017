from django.contrib.auth.models import User
from django import forms
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Brukernavn / Email', required=True, error_messages={'required': 'Vennligst fyll in dette feltet'})
    password = forms.CharField(label='Passord', widget=forms.PasswordInput, required=True)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='* Passord', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='* Gjenta Passord', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': '* Brukernavn',
            'first_name': '* Fornavn',
            'last_name': '* Etternavn',
            'email': '* Email',
        }


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passordene stemmer ikke.')
        return cd['password2']


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'date_of_birth', 'photo')
        labels = {
            'gender': '* Kjønn',
            'date_of_birth': '* Fødselsdato',
            'photo': 'Bilde',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['date_of_birth'].required = True


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