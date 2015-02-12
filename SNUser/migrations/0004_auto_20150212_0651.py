# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import SNUser.models


class Migration(migrations.Migration):

    dependencies = [
        ('SNUser', '0003_snuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snuser',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=SNUser.models.get_file_path, blank=True),
            preserve_default=True,
        ),
    ]
