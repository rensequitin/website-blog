from django import forms
from .models import PostModel

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title','content']