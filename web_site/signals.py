from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user_ref=instance)
        user_profile.friends.add(instance)
        return user_profile