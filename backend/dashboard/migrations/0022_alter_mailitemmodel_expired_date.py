# Generated by Django 3.2.23 on 2024-03-06 07:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_auto_20240227_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailitemmodel',
            name='expired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 6, 7, 0, 22, 389988, tzinfo=utc)),
        ),
    ]
