# Generated by Django 3.2.23 on 2024-03-16 07:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_auto_20240310_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailitemmodel',
            name='date_of_receipt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mailitemmodel',
            name='expired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 16, 7, 31, 10, 120205, tzinfo=utc)),
        ),
    ]