from django.contrib import admin
# from the housesApp, and in the models file, import the class houselistingModel
from .models import houselistingModel 

# Register your models here.
#admin.site.register(houselistingModel)

@admin.register(houselistingModel)
class houselistingAdmin(admin.ModelAdmin):
    #Customizing the admin site
    # Displays th following in admin site
    list_display = ('title', 'price', 'square_feet', 'no_of_bedrooms', 'address')

