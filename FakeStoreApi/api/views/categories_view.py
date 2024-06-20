from rest_framework import generics
from rest_framework.permissions import AllowAny
from api.serializers.category_serializer import *

class CategoriesView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

