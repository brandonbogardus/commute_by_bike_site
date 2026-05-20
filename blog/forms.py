from django import forms
from django.forms import inlineformset_factory
from .models import Post, PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]           # only expose these two fields to the user
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),          # Bootstrap styling
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        }


# Inline formset allowing up to 3 images to be uploaded with a post
PostImageFormSet = inlineformset_factory(
    parent_model=Post,
    model=PostImage,
    fields=["image", "caption"],
    extra=3,        # show 3 blank image upload fields
    can_delete=True,
)
