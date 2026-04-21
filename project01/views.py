from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')
def home(request):
    return render(request, 'home.html')


def registration(request):
    ...


def login_view(request):
    ...


def dashboard(request):
    ...


def logout_view(request):
    ...