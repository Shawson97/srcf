# Generated by Django 3.1.2 on 2020-12-03 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20201203_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='Education',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='First name',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='Last name',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='Work as',
        ),
        migrations.RemoveField(
            model_name='upload',
            name='bio',
        ),
    ]
