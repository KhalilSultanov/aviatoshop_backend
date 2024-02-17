from django.contrib import admin
from django.urls import path
from aviatoProject.apps.shopAviato.views import products, product, products_by_category, trending_products, categories, \
    search_products, product_photos, product_by_title_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products, name='products'),
    path('product/<int:id>/', product, name='product'),
    path('products/category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('trending/', trending_products, name='trending_products'),
    path('categories/', categories, name='categories'),
    path('products/search/', search_products, name='search_products'),
    path('product/<int:product_id>/photos/', product_photos, name='product-photos'),
    path('product_by_name/', product_by_title_name, name='product-by-title-name'),
]
