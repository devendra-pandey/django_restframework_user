from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from datetime import  date
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.functions import Now
from django.utils.translation import gettext_lazy as _

# class Profile(AbstractUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=50)
#     gender = models.BooleanField(default=True)
#     dob = models.DateField(
#         help_text=_('Enter the date of birt'),
#         validators=[MaxValueValidator(limit_value=date.today)],
#         verbose_name=_('Date of Birth')
#     )
#
#     class Meta:
#         constraints = [
#             models.CheckConstraint(
#                 check=models.Q(dob__lte=Now()),
#                 name='date_of_birth_cannot_be_future_date'
#             )
#         ]



@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )