from django import forms
from Posts.models import Post
import bleach

class PostForm(forms.ModelForm):
    def clean_body(self):
        return bleach.clean(self.cleaned_data.get('body'), strip=True)
    class Meta:
        model = Post
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows': 2})
        }
