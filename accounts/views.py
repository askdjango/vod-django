# accounts/views.py
from django.shortcuts import render


def profile(request):
    return render(request, 'accounts/profile.html')

