from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
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

def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    # obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../all/')
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        'object_list': queryset
    }
    return render(request, 'products/product_list.html', context)
