from django.urls import path
from . import views

# pk --- primary key
urlpatterns = [
     path('', views.houselistings, name = "home"),
     path('details/<pk>/', views.retreiveDetails, name = "details"),
]
   
