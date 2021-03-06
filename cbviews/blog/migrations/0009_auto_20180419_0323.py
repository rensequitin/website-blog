# Generated by Django 2.0.2 on 2018-04-19 03:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180419_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 4, 19, 3, 23, 44, 134685, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'blank': 'This field is not full, please try again.', 'unique': 'This title is not unique, please try again.'}, help_text='Must be a unique title.', max_length=240, unique=True, verbose_name='Post title'),
        ),
    ]
