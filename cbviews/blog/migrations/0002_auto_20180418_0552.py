# Generated by Django 2.0.2 on 2018-04-18 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(),
        ),
    ]
