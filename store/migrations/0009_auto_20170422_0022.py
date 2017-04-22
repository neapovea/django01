# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='latitude',
            field=models.FloatField(default=b'37.41920', max_length=20),
        ),
        migrations.AddField(
            model_name='review',
            name='longitude',
            field=models.FloatField(default=b'122.05740', max_length=20),
        ),
    ]
