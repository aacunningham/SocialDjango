from django import forms
from Posts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2})
        }
