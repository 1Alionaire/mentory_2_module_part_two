from django import forms
from Posts.models import Post

class InputBlogRecord(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ('title', 'content')

