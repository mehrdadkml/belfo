from datetime import datetime, timedelta,timezone

from random import choices
from time import timezone
from tokenize import blank_re
from django.db import models
from django.contrib.auth import get_user_model
from ..core.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField
from django.core.cache import cache
from django.conf import settings
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator

User=get_user_model()


class Profile (TimeStampedModel):
    GENDER_MALE='m'
    GENDER_FEMALE='f'

    GENDER_CHOICES=(
        (GENDER_MALE,'آقا'),
        (GENDER_FEMALE,'خانم'),

    )

    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    phone_number=PhoneNumberField(blank=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True)
    
    def __str__(self):
        return '%s'% self.user.username

    @property

    def last_seen(self):
        return cache.get(f'seen_{self.user.username}')

    @property

    def online(self):
        if self.last_seen:
            now=datetime.now(timezone.irdt)
            if now>self.last_seen + timedelta(minutes=settings.USER_ONLINE_TIMEOUT):
                return False
            else:
                return True
        else:
            return False



class Address(TimeStampedModel):
    user=models.ForeignKey(User,related_name='addres',on_delete=models.CASCADE)
    country=CountryField(blank=False,null=False)
    city=models.CharField(max_length=50,blank=False,null=False)
    street_address=models.CharField(max_length=300,blank=False,null=False)
    postal_code=models.CharField(max_length=30,null=True,blank=True)
    phone_number=PhoneNumberField(null=True,blank=True)
    building_number=models.IntegerField(blank=False,null=False,validators=[MinValueValidator(1)])
    apartment_number = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])









# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, *args, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)




# pre_save = ModelSignal(use_caching=True)
# post_save = ModelSignal(use_caching=True)