# Generated by Django 3.2 on 2021-05-08 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_projects_categ'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='lang',
            field=models.CharField(default='python', max_length=100),
        ),
    ]