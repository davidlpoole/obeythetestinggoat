# Generated by Django 4.2.2 on 2023-06-18 21:14

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=40),
        ),
    ]
