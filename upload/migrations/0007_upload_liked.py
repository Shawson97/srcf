# Generated by Django 3.1.2 on 2020-12-21 13:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0006_delete_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='liked',
            field=models.ManyToManyField(related_name='public_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]