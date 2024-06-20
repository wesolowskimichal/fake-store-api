from rest_framework import generics
from api.models import ProductImage, Product
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers.product_serializer import *

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(seller=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(seller=self.request.user)
        else:
            print(serializer.error)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductDetailsSerializer
    

    