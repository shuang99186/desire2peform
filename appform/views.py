from django.shortcuts import render


def programs(request):
    return render(request, 'application/programs.html', {})

def home(request):
    return render(request, 'application/home.html', {})
