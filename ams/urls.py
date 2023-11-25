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

app_name = 'ams'

urlpatterns = [
    path('assets', views.AssetList.as_view(), name='asset_create'),
    path('asset/<int:pk>/', views.AssetDetail.as_view(), name='asset_detail'),
    path('bundles/', views.BundleList.as_view(), name='bundle_create'),
    path('bundle/<int:pk>/', views.BundleDetail.as_view(), name='bundle_detail'),
    path('products/', views.ProductList.as_view(), name='product_create'),
    path('product/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
]