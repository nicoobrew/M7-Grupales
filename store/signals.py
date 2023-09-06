from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order


@receiver(post_save, sender=Order)
def send_order_status_email(sender, instance, **kwargs):
    order_status = instance.estado_pedido
    if order_status in [status[0] for status in Order.order_status]:
        subject = f"Actualización de estado de pedido #{instance.id}"
        message = f"Tu pedido número {instance.id} ha sido actualizado a: {order_status}."
        send_mail(subject, message, settings.EMAIL_HOST_USER, [instance.email])
