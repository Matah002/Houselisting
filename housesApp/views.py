from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.
"""
CRUD - Create/Retrieve, Update, Delete

"""
# List all the houses
def listing_list(request):
    # select * from houselistingModel/table
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    
    return render(request, 'listings.html', context)
# listing.objects.get(id=pk)
#CRUD - Read/Retrieve views
#view each house by itself
def listing_retrieve(request, pk):
    #get the house by id
    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }

    return render(request, 'listing.html', context)

# Create views
def listing_create(request):
    form = ListingForm()  # by default it creates an empty list
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES) # request.FILES >>> for images to work,, update also on this template
        if form.is_valid():
            form.save()
            return redirect("/")  # "/" >>> redirects to homepage
        
    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)


# Update views
def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)  # by default it creates an empty list 
    # instance = listing >>>> Django knows we are updating an existing form, we are not creating a new one
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")  # "/" >>> redirects to homepage
        
    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)


# Deleting views
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/")




