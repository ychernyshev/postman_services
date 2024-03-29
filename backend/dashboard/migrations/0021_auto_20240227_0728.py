# Generated by Django 3.2.23 on 2024-02-27 05:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20240224_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipientmodel',
            name='company_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='mailitemmodel',
            name='expired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 27, 5, 28, 28, 298510, tzinfo=utc)),
        ),
    ]
