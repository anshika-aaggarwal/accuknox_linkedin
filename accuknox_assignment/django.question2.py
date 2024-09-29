# signals.py
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    current_thread = threading.current_thread().name
    print(f"Signal executed in thread: {current_thread}")

# view.py
from django.contrib.auth.models import User

def save_user(request):
    user = User.objects.create(username="testuser")
    current_thread = threading.current_thread().name
    print(f"View executed in thread: {current_thread}")
    return HttpResponse("User created")


