from django.shortcuts import render

def home(request):
    names = ['Chris', 'Katie', 'Joe']
    #this is the context dictionary
    return render(request, 'pages/home.html', {'names': names})

