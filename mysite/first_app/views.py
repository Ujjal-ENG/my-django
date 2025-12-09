from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request) -> HttpResponse:
    return HttpResponse("Welcome to the Blog Home Page!")