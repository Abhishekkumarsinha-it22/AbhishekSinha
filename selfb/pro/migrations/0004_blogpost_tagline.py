# Generated by Django 3.2 on 2021-05-07 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0003_blogpost_bwholepost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tagline',
            field=models.TextField(default='tagline'),
        ),
    ]
