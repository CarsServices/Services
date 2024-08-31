"""
URL configuration for autocarmax project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import urls as users_app_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('', include(users_app_urls))

]
if settings.DEBUG: # since i will be using AWS for hosting this site  the functo=ion will apply to only  this if the degug is true
    urlpatterns += static(settings.MEDIA_ROOT, document_root= settings.MEDIA_URL)