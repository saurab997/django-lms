"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from library.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', author_list, name='author_list'),
    path('authors/new/', author_create, name='author_create'),
    path('authors/<int:pk>/', author_detail, name='author_detail'),
    path('authors/<int:pk>/edit/', author_update, name='author_update'), 
    path('authors/<int:pk>/delete/', author_delete, name='author_delete'),

    path('books/', book_list, name='book_list'),
    path('books/new/', book_create, name='book_create'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('books/<int:pk>/edit/', book_update, name='book_update'), 
    path('books/<int:pk>/delete/', book_delete, name='book_delete'),
 ]
