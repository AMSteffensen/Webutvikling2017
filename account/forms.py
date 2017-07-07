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

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        # Default css class attributes
        for field in self.fields.values():
            field.widget.attrs['class'] = ""

        # Labels
        self.fields['username'].label = '* Brukernavn'
        self.fields['first_name'].label = '* Fornavn'
        self.fields['last_name'].label = '* Etternavn'
        self.fields['email'].label = '* Email'

        # Required Fields
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        # Help Texts
        self.fields['username'].help_text = 'Kan ikke være lenger enn 22 karakterer.<br>Kan ikke inneholde spesialkarakterer !,@,#,$,&,%,(,}...'
        self.fields['password'].help_text = 'Kan ikke være mindre enn 7 karakterer.<br>Må inneholde både store og små bokstaver samt tall.'

        # Placeholders
        self.fields['username'].widget.attrs['placeholder'] = 'e.g. Joe'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'

        # Error Messages

        # HTML5 Required Popup
        #for field in self.fields.values():
        #    field.widget.attrs['oninvalid'] = 'this.setCustomValidity("{} er påkrevd")'.format(field.label.replace('*', '').strip())
        #    field.widget.attrs['oninput'] = 'this.setCustomValidity("")'

    # Verify Password
    def clean_password(self):
        print("cleaning password1")
        pwd = self.cleaned_data
        # Check if password is at least 7 characters long
        if len(cd['password']) < 7:
            self.fields['password'].widget.attrs['class'] = "cFormInputError"
            raise forms.ValidationError('Passordet må være minst 7 karakterer langt')
        # Check if password contains at least one lower case letter
        if not any(x.islower() for x in cd['password']):
            self.fields['password'].widget.attrs['class'] = "cFormInputError"
            raise forms.ValidationError('Passordet må inneholde minst én liten bokstav')
        # Check if password contains at least one upper case letter
        if not any(x.isupper() for x in cd['password']):
            self.fields['password'].widget.attrs['class'] = "cFormInputError"
            raise forms.ValidationError('Passordet må inneholde minst én stor bokstav')
        # Check if password contains at least one didgit
        if not any(x.isdigit() for x in cd['password']):
            self.fields['password'].widget.attrs['class'] = "cFormInputError"
            raise forms.ValidationError('Passordet må inneholde minste ett tall')
        return cd['password']


    # Verify Password2
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            self.fields['password2'].widget.attrs['class'] = "cFormInputError"
            raise forms.ValidationError('Passordene stemmer ikke.')
        return cd['password2']


    # Verify Email
    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            self.fields['email'].widget.attrs['class'] = "cFormInputError"
            raise forms.ValidationError('Det eksisterer allerede en bruker med denne mailen.')
        return cd['email']


class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'date_of_birth', 'photo')

    def __init__(self, *args, **kwargs):
        super(ProfileRegistrationForm, self).__init__(*args, **kwargs)

        # Labels
        self.fields['gender'].label = '* Kjønn'
        self.fields['date_of_birth'].label = '* Fødselsdato'
        self.fields['photo'].label = 'Bilde'

        # Required Fields
        self.fields['gender'].required = True
        self.fields['date_of_birth'].required = True

        # Placeholders
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'dd.mm.yyyy'


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
