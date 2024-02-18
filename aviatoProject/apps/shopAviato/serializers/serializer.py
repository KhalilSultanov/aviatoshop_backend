from rest_framework import serializers

from aviatoProject.apps.shopAviato.models.product import Product, Category, Photos


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    main_photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Photos
        fields = ['photo', 'main_photo_url']
    
    def get_main_photo_url(self, obj):
        request = self.context.get('request')
        product_id = self.context.get('product_id')
        product = Product.objects.get(pk=product_id)
        if product.main_photo and hasattr(product.main_photo, 'url'):
            return request.build_absolute_uri(product.main_photo.url)
        else:
            return None
