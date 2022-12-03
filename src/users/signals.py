from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, post_migrate, post_init
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
