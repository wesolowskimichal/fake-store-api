from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from api.serializers.category_serializer import *

class CategoryAddView(generics.CreateAPIView):
    """
    For Admin users only. Creating new Categoy
    """
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    
class CategoryEditView(generics.RetrieveUpdateDestroyAPIView):
    """
    Editing and deleteing Category is only for Admin users. 
    Getting is for all users. 
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field='id' 

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]