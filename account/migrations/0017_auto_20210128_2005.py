# Generated by Django 3.1.2 on 2021-01-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20210123_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='no_image.png', null=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
