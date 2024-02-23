from django.contrib import admin
from django.urls import path, include  # Используйте include для разделения URL конфигурации по приложениям
from django.conf import settings
from django.conf.urls.static import static
from aviatoProject.apps.shopAviato import views

# Определяем URL-адреса, специфичные для приложения, в отдельном файле (например, shopAviato/urls.py)
# и включаем их здесь с префиксом 'api/'
shop_aviato_urls = [
    path('products/', views.products, name='products'),
    path('product/<int:id>/', views.product, name='product'),
    path('products/category/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('trending/', views.trending_products, name='trending_products'),
    path('categories/', views.categories, name='categories'),
    path('products/search/', views.search_products, name='search_products'),
    path('product/<int:product_id>/photos/', views.product_photos, name='product-photos'),
    path('product_by_name/', views.product_by_title_name, name='product-by-title-name'),
]

urlpatterns = [
    path('admin/', admin.site.urls),  # Удалите 'api/' из пути админ-панели
    path('api/', include(shop_aviato_urls)),  # Используйте include для API-путей
]

# Добавляем маршруты для медиафайлов только в режиме DEBUG
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

