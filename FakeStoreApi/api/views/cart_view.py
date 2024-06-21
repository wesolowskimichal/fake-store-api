from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, HttpResponse
from rest_framework.response import Response

from api.serializers.cart_serializer import *
    
class CartRetrieveView(generics.RetrieveAPIView):
    serializer_class = CartDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return cart
    
class CartAddProductView(generics.GenericAPIView):
    serializer_class = CartAddProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        
        try:
            cart_product = CartProduct.objects.get(cart=cart, product=product)
            new_quantity = cart_product.quantity + quantity
        except CartProduct.DoesNotExist:
            new_quantity = quantity
        
        if new_quantity > product.quantity:
            return Response({"status": "error", "message": "Requested quantity exceeds available stock."}, status=status.HTTP_400_BAD_REQUEST)
        
        cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
        cart_product.quantity = new_quantity
        cart_product.save()

        cart_product_serializer = CartProductDetailsSerializer(cart_product)
        
        return Response(cart_product_serializer.data, status=status.HTTP_200_OK)
    
class CartRemoveProductView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field='id'

    def get_queryset(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return CartProduct.objects.filter(cart=cart)
    
    def delete(self, request, *args, **kwargs):
        cart_product = get_object_or_404(self.get_queryset(), id=kwargs['id'])
        cart_product.delete()
        return Response({"status": "success", "message": "Product removed from cart"}, status=status.HTTP_200_OK)
    
    
    

class CartEditProdcutView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_field='id'
    serializer_class = CartProductDetailsSerializer

    def get_queryset(self):
        user = self.request.user
        cart, created = Cart.objects.get_or_create(user=user)
        return CartProduct.objects.filter(cart=cart)