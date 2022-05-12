from django import forms
from django.forms import ModelForm
from .models import Article



class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'created_on' : forms.HiddenInput(attrs={'class':'form-control'}),
            'section' : forms.Select(attrs={'class':'form-control'}),
        }