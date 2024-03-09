# Generated by Django 3.2.23 on 2024-03-07 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_auto_20240306_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailitemmodel',
            name='expired_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 7, 9, 25, 36, 786531, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='recipientmodel',
            name='build',
            field=models.CharField(blank=True, choices=[('', ''), ('tpo', 'До відділення'), ('3', '3'), ('5', '5'), ('7', '7'), ('9', '9'), ('11', '11'), ('13', '13'), ('15', '15'), ('17', '17'), ('20', '20'), ('25', '25'), ('27', '27'), ('73', '73'), ('75', '75'), ('77', '77'), ('81', '81'), ('85', '85'), ('87', '87'), ('89', '89'), ('91', '91'), ('93', '93'), ('99', '99'), ('101', '101'), ('103', '103'), ('105', '105'), ('107', '107'), ('111', '111'), ('113', '113'), ('115', '115'), ('117', '117'), ('123', '123'), ('127', '127'), ('133', '133'), ('260', '260'), ('262', '262'), ('264', '264'), ('266', '266'), ('268', '268'), ('270', '270'), ('272', '272'), ('274', '274'), ('276', '276'), ('278', '278'), ('280', '280'), ('282', '282'), ('284', '284'), ('286', '286'), ('288', '288'), ('290', '290'), ('292', '292'), ('294', '294'), ('296', '296'), ('298', '298'), ('300', '300'), ('302', '302'), ('304', '304'), ('306', '306'), ('308', '308'), ('310', '310'), ('312', '312'), ('314', '314'), ('316', '316'), ('318', '318'), ('320', '320'), ('322', '322'), ('324', '324'), ('326', '326'), ('328', '328'), ('330', '330')], default='', max_length=3),
        ),
    ]
