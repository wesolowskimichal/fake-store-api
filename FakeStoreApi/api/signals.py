from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import User, Cart

@receiver(post_save, sender=User)
def create_cart_for_new_user(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)