from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    # widgets_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets})

# def widget_detail(request, widget_id):
#     widget = Widget.objects.get(id=widget_id)
#     return render(request, 'detail.html', {'widget': widget,})    

class WidgetCreate(CreateView):
    model = Widget 
    fields='__all__'
    success_url = '/'


class WidgetDelete(DeleteView):
  model = Widget
  success_url = '/'

   