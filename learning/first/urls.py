from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login')
]