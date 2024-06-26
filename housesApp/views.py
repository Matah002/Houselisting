from django.shortcuts import render
from .models import houselistingModel

# Create your views here.
"""
CRUD - Create/Retrieve, Update, Delete

"""
# List all the houses
def houselistings(request):
    # select * from houselistingModel/table
    listings = houselistingModel.objects.all()
    context = {
        "listings": listings,
    }
    
    return render(request, 'listings.html', context)

#CRUD - Read/Retrieve
#view each house by itself
def retreiveDetails(request, pk):
    #get the house by id
    specific_house =houselistingModel.objects.get(id = pk)
    context = {
        "specific": specific_house
    }
    return render(request, 'details.html', context)



