from django import forms
from .models import Job_Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Job_Comment
        fields = ('name','email','body')