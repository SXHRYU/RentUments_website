from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, 'products/product_create.html', context)
    
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

# Create your views here.
def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=37)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

def dynamic_lookup_view(request):
    obj = Product.objects.get(id=37)
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)
