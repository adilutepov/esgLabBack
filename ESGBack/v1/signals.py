from django.db.models.signals import post_save
from django.dispatch import receiver

<<<<<<< HEAD
from .models import News, Subscriber
from .services import send_news_notification_email
=======
from .models import News
from .services import get_news_notification_recipients, send_news_notification_email
>>>>>>> esgtest-r/main


@receiver(post_save, sender=News)
def send_news_to_subscribers(sender, instance, created, **kwargs):
    if not created:
        return

<<<<<<< HEAD
    recipient_list = list(Subscriber.objects.filter(is_active=True).values_list("email", flat=True))
=======
    recipient_list = get_news_notification_recipients(instance)
>>>>>>> esgtest-r/main
    send_news_notification_email(instance, recipient_list)
