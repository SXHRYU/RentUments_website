from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": ['apple', 'orange', 2222]
    }
    return render(request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact_us.html", {})

def contacts_view(request, *args, **kwargs):
    return render(request, 'contacts.html', {})

def catalogue_view(request, *args, **kwargs):
    return render(request, 'catalogue.html', {})

def cart_view(request, *args, **kwargs):
    return render(request, 'cart.html', {})