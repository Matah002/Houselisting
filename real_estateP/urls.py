"""
URL configuration for real_estateP project.

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from housesApp.views import (
     listing_list, 
     listing_retrieve, 
     listing_create, 
     listing_update,
     listing_delete
)

# HousesApp >>>> name of my app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", listing_list),
    path('housesApp/<pk>/', listing_retrieve),
    path('add-listing/', listing_create),
    path('housesApp/<pk>/edit/', listing_update),
    path('housesApp/<pk>/delete/', listing_update),

]    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


