# Generated by Django 3.1.2 on 2020-12-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_profile_work as'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]