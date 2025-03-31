from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    ## username
    ## password가 이미 있는 것임
    profile_image = ResizedImageField(
        size = [500,500],
        crop = ['middle', 'center'],
        upload_to = 'profile'
    )
