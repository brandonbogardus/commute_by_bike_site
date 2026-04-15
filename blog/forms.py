from django import forms
from django.forms import inlineformset_factory
from .models import Post, PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        }


PostImageFormSet = inlineformset_factory(
    parent_model=Post,
    model=PostImage,
    fields=["image", "caption"],
    extra=3,
    can_delete=True,
)
