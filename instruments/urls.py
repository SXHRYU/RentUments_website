"""instruments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import (home_view, contact_view, contacts_view, 
                        about_view,  cart_view, catalogue_view)
from products.views import (product_delete_view, product_detail_view, 
                            product_create_view, dynamic_lookup_view, product_list_view)
from accounts.views import login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('admin/', admin.site.urls, name='admin'),
    path('cart/', cart_view, name='cart'),
    path('catalogue/', catalogue_view, name='catalogue'),
    path('contact/', contact_view, name='contact'),
    path('contacts/', contacts_view, name='contacts'),
    path('create/', product_create_view, name='create_products'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('products/', product_detail_view, name='products'),
    path('products/all/', product_list_view, name='list'),
    path('products/<int:id>/', dynamic_lookup_view, name='dynamic'),
    path('products/<int:id>/delete/', product_delete_view, name='delete'),
]
