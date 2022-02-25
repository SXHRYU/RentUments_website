from django.urls import path
from .views import (
    product_delete_view, 
    product_detail_view, 
    product_create_view, 
    dynamic_lookup_view, 
    product_list_view)

urlpatterns = [
    path('', product_detail_view, name='products-detail'),
    path('all/', product_list_view, name='products-list'),
    path('create/', product_create_view, name='products-create'),
    path('<int:id>/', dynamic_lookup_view, name='products-dynamic'),
    path('<int:id>/delete/', product_delete_view, name='products-delete'),
]