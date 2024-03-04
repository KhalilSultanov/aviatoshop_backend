from rest_framework import serializers

from aviatoProject.apps.shopAviato.models.product import Product, Category, Photos, Review, Size, Color, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'text', 'date_time']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['photo']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Добавляем поле для комментариев
    color = ColorSerializer(many=True, read_only=True)  # Добавляем поле для цветов
    size = SizeSerializer(many=True, read_only=True)  # Добавляем поле для размеров
    category = CategorySerializer(read_only=True)  # Добавляем поле для категории
    photos = PhotoSerializer(many=True, read_only=True)  # Добавляем поле для фотографий

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address']