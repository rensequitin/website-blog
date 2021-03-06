# Generated by Django 2.0.2 on 2018-04-19 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180418_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'blank': 'This field is not full, please try again.', 'unique': 'This title is not unique, please try again.'}, help_text='Must be a unique title.', max_length=240, unique=True),
        ),
    ]
