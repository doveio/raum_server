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
from django.urls import (path, include)

# Admin Site Config
admin.sites.AdminSite.site_header = 'RAUM'
admin.sites.AdminSite.site_title = 'Raum Admin'
admin.sites.AdminSite.index_title = 'Admin control panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/v1/', include('rest_framework.urls', namespace='rest_framework')),
    path('core/v1/', include('core.urls', namespace='core_api')),
    path('ams/v1/', include('ams.urls', namespace='ams_api')),

]