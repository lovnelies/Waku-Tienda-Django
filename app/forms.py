from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['author']
        fields = ['title', 'content', 'price', 'image']