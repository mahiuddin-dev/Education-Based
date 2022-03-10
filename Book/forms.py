from django import forms
from .models import Book_Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Book_Comment
        fields = ('name','email','body')