from django.shortcuts import render, redirect
from .models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        confirmation = request.POST["password2"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        if password != confirmation:
            return render(
                request, "cargo/register.html", {"message": "Passwords do not match"}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "cargo/register.html", {"message": "Username already taken"}
            )

        # Log in the user after successful registration
        auth_login(request, user)
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return render(request, "cargo/register.html")


def index(request):
    return render(request, "cargo/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(
                request,
                "cargo/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "cargo/login.html")


def dashboard(request):
    return render(request, "cargo/dashboard.html")


def logout_view(request):
    return render(request, "cargo/login.html")
