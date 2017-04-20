# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20170420_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Book',
            new_name='book',
        ),
    ]
