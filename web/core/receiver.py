# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.core.mail import send_mail
#
#
# @receiver(post_save, sender=User)
# def send_welcome_email(sender, instance, created):
#     if created:
#         send_mail(
#             "Bienvenido",
#             "Te damos la bienvenida al sistema del diplomado BUAP",
#             "no_reply@diplomado_buap.com",
#             [instance.email],
#             fail_silently=False,
#         )
