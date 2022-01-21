from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widget

# Create your views here.
def index(request):
    return render(request, 'index.html')