from rest_framework import serializers
from api.models import Cart, CartProduct, Product
from api.serializers.product_serializer import ProductDetailsSerializer
from api.serializers.user_serializer import UserDetailsSerializer

class CartProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductDetailsSerializer(read_only=True)
    
    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'quantity']
        extra_kwargs = {
            'id': {'read_only': True}
        }


class CartDetailsSerializer(serializers.ModelSerializer):
    products = CartProductDetailsSerializer(source='cart_porducts', many=True)
    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'products']
        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
            'products': {'read_only': True}
        }

class CartAddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['product', 'quantity']

class CartProductEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ['quantity']