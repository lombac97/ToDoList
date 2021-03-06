"""ensolvers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic.base import RedirectView


#This handler is used to redirect to folder (and if user is not logged in, to login view)
#when tries to access to a non existing url. It is IMPORTANT to say that this only works
#on production, when debug is False
handler404 = 'accounts.views.handler404'

urlpatterns = [
    path('', RedirectView.as_view(url='toDoList/folders')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('toDoList/', include('to_do_list.urls'))  
]

