from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_view),
    path('registration/', views.registration),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout_view),
]

path('create-admin/', views.create_admin),