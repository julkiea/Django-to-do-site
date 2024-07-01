from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('login/', views.login_user, name = 'login'),
    path('add_task/', views.add_task, name = 'add_task'),
]