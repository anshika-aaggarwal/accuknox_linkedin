# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is running inside a database transaction")

# views.py
from django.db import transaction
from django.contrib.auth.models import User

def save_user(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username="testuser")
            raise Exception("Triggering rollback")
    except Exception as e:
        print(e)
    return HttpResponse("Done")
