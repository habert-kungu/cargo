from django.shortcuts import render

# acts as a helpers for logic
from . import util

# from django.http import HttpResponse


def index(request):
    return render(request, "cargo/index.html")


def register(request):
    return render(request, "cargo/register.html")


def login(request):
    return render(request, "cargo/login.html")
