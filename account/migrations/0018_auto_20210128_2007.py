# Generated by Django 3.1.2 on 2021-01-28 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210128_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='no_image.png', upload_to='users/%Y/%m/%d'),
        ),
    ]
