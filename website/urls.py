from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('login/', views.login_user, name = 'login'),
    path('add_task/', views.add_task, name = 'add_task'),
    path('task/<int:pk>/', views.task, name='task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:pk>/edit/', views.edit_task, name = 'edit_task'),
    path('task/<int:pk>/complete/', views.complete_task, name ='complete_task'),
    path('sort_tasks/<str:sort_by>/', views.sort_tasks, name ='sorted_task'),
]