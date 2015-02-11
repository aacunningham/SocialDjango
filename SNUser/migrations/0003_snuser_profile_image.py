# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SNUser', '0002_auto_20150205_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='snuser',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
    ]
