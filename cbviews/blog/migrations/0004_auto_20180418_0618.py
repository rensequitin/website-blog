# Generated by Django 2.0.2 on 2018-04-18 06:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180418_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 18, 6, 18, 38, 374088, tzinfo=utc)),
        ),
    ]
