from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def adoption(request):
    return render(request,'adoption.html')

def advice(request):
    return render(request,'advice.html')

def pets(request):
    return render(request,'pets.html')

def login(request):
    return render(request,'login.html')

def shop(request):
    return render(request,'shop.html')