# Generated by Django 3.2 on 2021-05-18 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('selffp', '0009_alter_testimonial_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='img',
        ),
    ]