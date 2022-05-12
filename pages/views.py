from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from articles.models import Article
from .models import *


class Home(ListView):
    template_name = 'pages/home.html'
    model = Article
    context_object_name = 'articles'


class About(TemplateView):
    template_name = 'pages/about.html'