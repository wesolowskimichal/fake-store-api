from rest_framework import generics, filters
from rest_framework.response import Response
from api.models import ProductImage, Product
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers.product_serializer import *
from rest_framework.pagination import PageNumberPagination


class ProductListPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'page_info': {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'current_page': self.page.number,
                'last_page_number': self.page.paginator.num_pages,
            },
            'data': data
        })

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'price', 'createdAt']
    search_fields = ['title']
    pagination_class = ProductListPagination

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
    

    