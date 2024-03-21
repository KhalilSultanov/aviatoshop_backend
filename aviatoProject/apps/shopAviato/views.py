from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.product import Product, Category, Purchuase, PurchuaseQuntity, ContactForm
from .serializers.serializer import ProductSerializer, CategorySerializer, PhotoSerializer, ContactFormSerializer
from django.db import connections
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json





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


# views.py
@api_view(['GET'])
def product_by_title_name(request):
    title = request.query_params.get('title_en')  # изменение параметра на 'title_en'
    if title:
        products = Product.objects.filter(title_en__icontains=title)  # изменение поля на 'title_en'
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "Product title not specified"}, status=400)



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

@api_view(['GET'])
def search_products(request):
    query = request.query_params.get('q', '').lower()

    if query:
        def lower_function(s):
            return str(s).lower()

        with connections['default'].cursor() as cursor:
            cursor.connection.create_function('lower', 1, lower_function)
            products = Product.objects.raw(
                'SELECT * FROM shopaviato_product WHERE '
                'lower(title_ru) LIKE %s OR lower(title_az) LIKE %s OR lower(title_en) LIKE %s',
                ['%' + query + '%', '%' + query + '%', '%' + query + '%']
            )
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
    else:
        return Response([])



@api_view(['GET'])
def product_photos(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'message': 'Товар не найден'}, status=404)

    photos = product.photos.all()
    serializer = PhotoSerializer(photos, many=True, context={'product_id': product_id, 'request': request})
    return Response(serializer.data)


@csrf_exempt
def purchase_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        purchase = Purchuase.objects.create(
            fullname=data.get('fullname', ''),
            phone_number=data.get('phone_number', ''),
            message=data.get('message', ''),
            address=data.get('address', '')
        )

        for product_id, quantity in data.get('products', {}).items():
            product = Product.objects.get(pk=product_id)
            purchase_quantity = PurchuaseQuntity.objects.create(product=product, quantity=quantity)
            purchase.products.add(purchase_quantity)
            products_data = [{'id': item.product.id, 'name': item.product.title_en, 'quantity': item.quantity} for item
                             in purchase.products.all()]

        return JsonResponse({'message': 'Purchase created successfully', 'products': products_data})
    else:
        return JsonResponse({'message': 'Invalid request method'})




@csrf_exempt
def contact_form_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        serializer = ContactFormSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success': True, 'message': 'Contact form submitted successfully.'}, status=201)
        else:
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed.'}, status=405)
