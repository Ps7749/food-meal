"""
URL configuration for meal1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from order import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.aboutpage, name='about'),
    path('menu/', views.menupage, name='menu'),
    path('order/', views.orderpage, name='order'),
    path('io1/', views.io1page, name='io1'),
    path('style2/', views.style2page, name='style2'),
    path('contact/', views.contactpage, name='contact'),
]
