from django.db import models
from SNUser.models import SNUser
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    owner = models.ForeignKey(SNUser)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=timezone.now())

    def __unicode__(self):
        return self.body[0:40]
