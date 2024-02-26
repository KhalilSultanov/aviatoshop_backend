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
    class Meta:
        model = Photos
        fields = ['photo']
