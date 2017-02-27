# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render


def mysum(request, numbers):
    # numbers = "1/2/12/123/12312/312/123123"
    # result = sum(map(int, numbers.split("/")))
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)
