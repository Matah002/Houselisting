#Create
from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "square_feet",
            "no_of_bedrooms",
            "address",
        ]

        