from django.contrib import admin
from django.urls import path
from aviatoProject.apps.shopAviato.views import products, product, products_by_category, trending_products, categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products, name='products'),
    path('product/<int:id>/', product, name='product'),
    path('products/category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('trending/', trending_products, name='trending_products'),
    path('categories/', categories, name='categories'),
]
