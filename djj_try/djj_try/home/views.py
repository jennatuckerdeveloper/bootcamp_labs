from django.shortcuts import render
from .models import Thing

def home(request):
    things = Thing.objects.all()
    return render(request, 'home/home.html', {'things': things})
