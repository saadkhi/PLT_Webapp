from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def careers(request):
    return render(request, 'careers.html')

def services(request):
    return render(request, 'services.html')

def industries(request):
    return render(request, 'industries.html')

def insights(request):
    return render(request, 'insights.html')
