import uuid
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        self.first_name
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
    rating = models.FloatField(default=10.0, validators=[MinValueValidator(1,0), MaxValueValidator(10.0)])
