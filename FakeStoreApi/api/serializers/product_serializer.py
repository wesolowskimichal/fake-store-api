from rest_framework import serializers
from api.models import Product, ProductImage
from api.serializers.category_serializer import CategorySerializer

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']
        extra_kwargs = {
            'id': {'read_only': True},
        }

class ProductDetailsSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'category', 'images', 'seller', 'createdAt']
        extra_kwargs = {
            'id': {'read_only': True},
            'seller': {'read_only': True},
            'createdAt': {'read_only': True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['images']:
            representation['images'] = [{'id': "default-product-image", 'image': '/defaults/default-product.png'}]
        return representation
    

class ProductCreateSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'category', 'images', 'seller', 'createdAt']
        extra_kwargs = {
            'id': {'read_only': True},
            'seller': {'read_only': True},
            'createdAt': {'read_only': True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['images']:
            representation['images'] = [{'id': "default-product-image", 'image': '/defaults/default-product.png'}]
        return representation