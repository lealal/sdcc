from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'club_site/home.html', context)

