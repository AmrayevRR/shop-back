from django.urls import path

from api.views import product_list, products_detail, category_list, categories_detail

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', products_detail),
    path('categories/', category_list),
    path('categories/<int:category_id>', categories_detail)
]
