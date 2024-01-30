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
    # Implement logic to get trending products
    return Response([])


@api_view(['GET'])
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(all_categories, many=True)
    return Response(serializer.data)
