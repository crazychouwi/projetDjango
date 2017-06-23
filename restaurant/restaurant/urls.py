"""restaurant URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^gestionPlat/', include('gestionPlat.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from gestionPlat import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurant.views.home', name='home'),
    # url(r'^gestionPlat/', include('gestionPlat.urls')),
    url(r'^accueil$', views.home),
    url(r'^admin/', include(admin.site.urls)),
)
