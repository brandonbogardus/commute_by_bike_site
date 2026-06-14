from django import forms
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),          # Bootstrap styling
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]