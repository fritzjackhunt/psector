from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'promosector/home.html')

def aboutus(request):
    return render(request, 'promosector/aboutus.html')

def contacts(request):
    return render(request, 'promosector/contacts.html')

def events(request):
    return render(request, 'promosector/events.html')

def news(request):
    return render(request, 'promosector/news.html')