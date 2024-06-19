from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.serializers.user_serializer import *

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes  = [AllowAny]

class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user
    
    def get_object(self):
        return self.get_queryset()
    
    def get_serializer_class(self):
        if(self.request.method == 'PUT'):
            return UserUpdateSerializer
        return UserDetailsSerializer
    

