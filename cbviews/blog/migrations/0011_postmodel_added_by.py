# Generated by Django 2.0.2 on 2018-04-19 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180419_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='added_by',
            field=models.CharField(default='Anonymous', max_length=240),
        ),
    ]
