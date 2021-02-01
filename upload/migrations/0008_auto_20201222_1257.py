# Generated by Django 3.1.2 on 2020-12-22 11:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0007_upload_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='like_count',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='upload',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='public_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
