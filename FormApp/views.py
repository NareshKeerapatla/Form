from django.shortcuts import render
from django.views.generic import CreateView
from .forms import FormClass
from .models import ModelClass
class Index(CreateView):
    model = ModelClass
    form_class = FormClass
    template_name = 'input.html'
    success_url = '/'


