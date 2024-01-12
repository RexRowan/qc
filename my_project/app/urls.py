from django.urls import path
from .views import index, section
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('section/<int:num>/', views.section, name='section'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('toggle-completion/<int:content_id>/', views.toggle_completion, name='toggle_completion'),
    path('sections/<int:section_id>/contents/', views.section_contents, name='section_contents'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('community/', views.community, name='community'),
]
