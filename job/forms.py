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

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['body'].required = True
        self.fields['status'].required = True