from django.urls import path
from .views import index, section

urlpatterns = [
    path('', index, name='index'),
    path('section/<int:num>/', section, name='section'),
]
