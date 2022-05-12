from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import *


class Home(TemplateView):
    template_name = 'pages/home.html'


class About(TemplateView):
    template_name = 'pages/about.html'