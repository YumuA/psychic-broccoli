from django.urls import path 
from . import views

urlpatterns = [
    path('', views.routes),
    path('posts/', views.routes),
    path('post/<int:id>', views.routes),
]