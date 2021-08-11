# Generated by Django 3.2 on 2021-05-07 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recname', models.CharField(max_length=100)),
                ('rectech', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('disc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('cont1', models.TextField()),
                ('cont2', models.TextField()),
                ('proid', models.IntegerField()),
            ],
        ),
    ]