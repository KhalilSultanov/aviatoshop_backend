from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.product import Product, Category
from .serializers.serializer import ProductSerializer, CategorySerializer


@api_view(['GET'])
def products(request):
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def products_by_category(request, category_id):
    products_in_category = Product.objects.filter(category=category_id)
    serializer = ProductSerializer(products_in_category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def trending_products(request):
    products_in_trend = Product.objects.filter(trending=True)
    serializer = ProductSerializer(products_in_trend, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response(serializer.data)


from django.db import connection


@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('q', '').lower()

    if query:
        def lower_function(s):
            return str(s).lower()
        connection.connection.create_function('lower', 1, lower_function)
        products = Product.objects.raw(
            'SELECT * FROM shopaviato_product WHERE lower(title_ru) LIKE %s OR lower(title_az) LIKE %s',
            ['%' + query + '%', '%' + query + '%']
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response([])
