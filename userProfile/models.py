from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    profilePicture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username
