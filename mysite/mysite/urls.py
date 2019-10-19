"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from blog import views

urlpatterns = [
	path('category/<slug:slug>', views.category, name='category'),
	path('categories_list/', views.categories_list, name='categories_list'),
	path('rubriki/', views.rubriki, name='rubriki'),
	path('post/<slug:slug>', views.post_detail, name='post_detail'),
	path('', views.post_list, name='post_list'),    
	path('admin/', admin.site.urls),
]
