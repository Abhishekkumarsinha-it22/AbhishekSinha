# Generated by Django 3.2 on 2021-05-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categories_headintro_sharing'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='categ',
            field=models.CharField(default='python', max_length=100),
            preserve_default=False,
        ),
    ]
