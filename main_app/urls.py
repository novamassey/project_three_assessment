from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createwidget/', views.WidgetCreate.as_view(), name='widget_create'),
    path('delete/<int:pk>/', views.WidgetDelete.as_view(), name='widget_delete'),
]