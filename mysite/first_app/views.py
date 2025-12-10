from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
# Create your views here.
def home(request) -> HttpResponse:
    # return HttpResponse("Welcome to the Blog Home Page!")
    blog = Blog.objects.all()
    return render(request, "index.html", {"blogs": blog})