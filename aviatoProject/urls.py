from django.contrib import admin
from django.urls import path
from aviatoProject.apps.shopAviato.views import products, product, products_by_category, trending_products, categories, \
    search_products, product_photos, product_by_title_name

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/products/', products, name='products'),
    path('api/product/<int:id>/', product, name='product'),
    path('api/products/category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('api/trending/', trending_products, name='trending_products'),
    path('api/categories/', categories, name='categories'),
    path('api/products/search/', search_products, name='search_products'),
    path('api/product/<int:product_id>/photos/', product_photos, name='product-photos'),
    path('api/product_by_name/', product_by_title_name, name='product-by-title-name'),
]
