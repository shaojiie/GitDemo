from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view
from products.views import (
    product_detail_view,
    product_create_view,
    product_initial_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view
    )

app_name = "products"
urlpatterns = [
    path('<int:id>/', dynamic_lookup_view,name='product-detail'),
    path('<int:id>/delete/', product_delete_view,name='product-delete'),
    path('',product_list_view,name='product-list'),
    path('create/', product_create_view),
    path('initial/', product_initial_view),
]