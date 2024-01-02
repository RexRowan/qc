# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('layout/', views.layout, name='layout'),
    path("sections/<int:num>", views.section, name="section")
]