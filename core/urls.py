"""
URL configuration for raum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

app_name = 'core'

urlpatterns = [
    path('status', views.StatusList.as_view(), name='status_create'),
    path('status/<int:pk>/', views.StatusDetail.as_view(), name='status_detail'),
    path('asset_type', views.AssetTypeList.as_view(), name='asset_type_create'),
    path('asset_type/<int:pk>/', views.AssetTypeDetail.as_view(), name='asset_type_detail'),
    path('process', views.ProcessList.as_view(), name='process_create'),
    path('process/<int:pk>/', views.ProcessDetail.as_view(), name='process_detail'),
    path('element', views.ElementList.as_view(), name='element_create'),
    path('element/<int:pk>/', views.ElementDetail.as_view(), name='element_detail'),
    path('data_type', views.DataTypeList.as_view(), name='data_type_create'),
    path('data_type/<int:pk>/', views.DataTypeDetail.as_view(), name='data_type_detail'),
]
