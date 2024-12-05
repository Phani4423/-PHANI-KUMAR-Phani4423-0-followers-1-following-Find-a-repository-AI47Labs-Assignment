"""
URL configuration for assinment project.

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
from django.urls import path,include,re_path
from app.views import *
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('display/', display, name='display'),
    path('home/',views.Home.as_view(),name='home'),
    path('SchoolListView/',views.SchoolListView.as_view(),name='list'),

    
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    re_path('update/(?P<pk>\d+)/',views.SchoolUpdateView.as_view(),name='update'),
    re_path('delete/(?P<pk>\d+)/',views.SchoolDeleteView.as_view(),name='delete'),
    re_path('(?P<pk>\d+)/',views.SchoolDetailView.as_view(),name='detail'),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
