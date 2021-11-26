from django import forms

from .models import Discussion
#use ModelFrom
class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['name', 'email', 'body']