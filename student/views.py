from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def home(request):
    return render(request, 'home.html')

from .models import Student

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if Student.objects.filter(email=email).exists():
            return render(request, 'registration.html', {
                'error': 'Email already exists'
            })

        if password == confirm:
            Student.objects.create(
                name=name,
                email=email,
                password=password
            )
            return redirect('/login/')
        else:
            return render(request, 'registration.html', {
                'error': 'Password does not match'
            })

    return render(request, 'registration.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Student.objects.filter(email=email, password=password)

        if user:
            request.session['user_id'] = user[0].id   # 🔥 ADD THIS
            request.session['user_name'] = user[0].name
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'login.html')


def logout_view(request):
    request.session.flush()
    return redirect('/login/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/login/')

    return render(request, 'dashboard.html', {
        'name': request.session.get('user_name')
    })

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.http import HttpResponse
from django.contrib.auth.models import User

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@gmail.com", "admin123")
        return HttpResponse("Admin created successfully")
    return HttpResponse("Admin already exists")