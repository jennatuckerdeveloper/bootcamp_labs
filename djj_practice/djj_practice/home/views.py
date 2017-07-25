from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def home(request):
    book = Book.objects.all()
    return render(request, 'home/home.html', {'book': book})
