# signals.py
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"Signal started for user {instance.username}")
    time.sleep(5)  # Simulate a time-consuming task
    print(f"Signal finished for user {instance.username}")


