from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widget = Widget.objects.all()
    # widgets_form = WidgetForm()
    return render(request, 'index.html', {'widget': widget})

class WidgetCreate(CreateView):
    model = Widget 
    fields='__all__'
    success_url = '/'

