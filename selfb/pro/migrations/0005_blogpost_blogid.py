# Generated by Django 3.2 on 2021-05-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0004_blogpost_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blogid',
            field=models.IntegerField(default=0),
        ),
    ]
