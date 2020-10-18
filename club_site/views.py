from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'club_site/home.html', context)

def projects(request):
    context = {}
    return render(request, 'club_site/projects.html', context)

def join(request):
    context = {}
    return render(request, 'club_site/join.html', context)

def contact(request):
    context = {}
    return render(request, 'club_site/contact.html', context)
