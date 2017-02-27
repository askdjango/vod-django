# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, x, y=0, z=0):
    # request: HttpRequest
    print(x, y, z)
    return HttpResponse(int(x) + int(y) + int(z))
