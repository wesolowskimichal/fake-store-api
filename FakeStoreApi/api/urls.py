from api.views.user_view import *
from api.views.category_view import *
from api.views.categories_view import *
from api.views.product_view import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include


urlpatterns = [
    # User
    path('register/', UserRegisterView.as_view(), name='register'),
    path('user/', UserDetailsView.as_view(), name='userOperations'),
    # Token
    path('token/', TokenObtainPairView.as_view(), name='getToken'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refreshToken'),
    # Category
    path('category/', CategoryAddView.as_view(), name='addCategory'),
    path('category/<uuid:id>/', CategoryEditView.as_view(), name='categoryId'),
    # Categories
    path('categories/', CategoriesView.as_view(), name='getAllCategories'),
    # Products
    path('products/', ProductListCreateView.as_view(), name='Managing_products')
]
