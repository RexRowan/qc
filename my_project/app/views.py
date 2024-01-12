from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.http import Http404, HttpResponse
from django.conf import settings
import os
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Content, UserProgress, Section

User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def section(request, num):
    # Retrieve the Section object with the given id (num) or raise a 404 error if not found
    section = get_object_or_404(Section, pk=num)
    # Render the section_detail template with the section data
    return render(request, 'section_detail.html', {
        'section': section
    })

@login_required
def section_contents(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    contents = Content.objects.filter(section=section)
    return render(request, 'section_contents.html', {
        'section': section,
        'contents': contents
    })

@login_required
def dashboard(request):
    user_progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'user_progress': user_progress})


@login_required
def toggle_completion(request, content_id):
    content = get_object_or_404(Content, pk=content_id)
    progress, created = UserProgress.objects.get_or_create(user=request.user, content=content)
    progress.completed = not progress.completed
    progress.save()
    return redirect('dashboard')

def about(request):
    # Render the about page
    return render(request, 'about.html')

def contact(request):
    # Render the contact page
    return render(request, 'contact.html')

def careers(request):
    # Render the careers page
    return render(request, 'careers.html')

def community(request):
    # Render the community page
    return render(request, 'community.html')
