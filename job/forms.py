from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'status')
        labels = {
            'title': 'Tittel',
            'body': 'Text',
            'email': 'Email',
        }