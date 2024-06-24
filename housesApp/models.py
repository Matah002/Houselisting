from django.db import models

# Create your models here.
class houselistingModel(models.Model):
    # The attribute
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    square_feet = models.IntegerField()
    no_of_bedrooms = models.IntegerField()
    address = models.CharField(max_length=255)
    image = models.ImageField()
