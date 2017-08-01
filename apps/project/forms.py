from django import forms
from .models import Project


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'body', 'priority', 'extent', 'deadline', 'price')
        labels = {
            'title': 'Tittel',
            'body': 'Text',
            'priority': 'Prioritet',
            'extent': 'Størrelse',
            'deadline': 'Slutt Dato',
            'price': 'Pris',
        }

    def __init__(self, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['body'].required = True
        self.fields['priority'].required = True
        self.fields['extent'].required = True
        self.fields['deadline'].required = True
        self.fields['price'].required = True
