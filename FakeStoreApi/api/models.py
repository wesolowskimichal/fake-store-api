import uuid
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    def __str__(self):
        return self.username
    
    def upload_to(self, filename):
        return f'users/{self.id}/{filename}'
    
    def get_absolute_url(self):
        return reverse('user-details-id', kwargs={'id': self.pk})
    

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=upload_to, default='/defaults/user-default.jpg')
    first_name = models.CharField(help_text='Required. First name', unique=False, blank=False, max_length=150)
    last_name = models.CharField(help_text='Required. Last name', unique=False, blank=False, max_length=150)
    email = models.EmailField(help_text='Required. Email address', unique=True)
    rating = models.FloatField(default=10.0, validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])


# Category Model
class Category(models.Model):
    def __str__(self) -> str:
        return self.title
    
    def upload_to(self, filename):
        return f'categories/{self.id}/{filename}'
    
    def get_absolute_url(self):
        return reverse('category-details-id', kwargs={'id': self.pk})
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(help_text='Required. Category\'s name', unique=False, blank=False, max_length=150)
    image = models.ImageField(upload_to=upload_to, default='/defaults/category-default.jpg')


# Product Model
class Product(models.Model):
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('product-details-id', kwargs={'id': self.pk})
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(help_text='Required. Product\'s name', unique=False, blank=False, max_length=150)
    price = models.FloatField(help_text='Required. Product\'s price', unique=False, blank=False, validators=[MinValueValidator(0.0)])
    description = models.TextField(help_text='Product\'s description', blank=True)
    createdAt = models.DateTimeField(help_text='Publication time of product', auto_now_add=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name='products',on_delete=models.CASCADE)



# ProductImage Model
class ProductImage(models.Model):
    def __str__(self):
        return f'Image for {self.product.title}'
    
    def upload_to(self, filename):
        return f'products/{self.product.id}/{filename}'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, default='/defaults/product-default.jpg')

    