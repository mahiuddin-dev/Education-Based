from django import forms
from .models import Post_Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Post_Comment
        fields = ('name','email','body')