from django.contrib import admin
# from the housesApp, and in the models file, import the class houselistingModel
from .models import houselistingModel 

# Register your models here.
admin.site.register(houselistingModel)