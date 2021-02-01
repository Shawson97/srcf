# Generated by Django 3.1.2 on 2020-11-24 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, null=True, unique_for_date='publish')),
                ('Issn', models.SlugField(max_length=10)),
                ('Second Title', models.CharField(blank=True, max_length=250, null=True)),
                ('Points', models.IntegerField(default=1)),
                ('architecture and urbanistic', models.CharField(blank=True, max_length=1, null=True)),
                ('history', models.CharField(blank=True, max_length=1, null=True)),
                ('linguistics', models.CharField(blank=True, max_length=1, null=True)),
                ('literature', models.CharField(blank=True, max_length=1, null=True)),
                ('studies on culture and religion', models.CharField(blank=True, max_length=1, null=True)),
                ('studies on arts', models.CharField(blank=True, max_length=1, null=True)),
                ('automatic, electronic and electrotechnic', models.CharField(blank=True, max_length=1, null=True)),
                ('technical IT and telecomunication', models.CharField(blank=True, max_length=1, null=True)),
                ('chemical engineering', models.CharField(blank=True, max_length=1, null=True)),
                ('civil engineering and transport', models.CharField(blank=True, max_length=1, null=True)),
                ('material engineering', models.CharField(blank=True, max_length=1, null=True)),
                ('mechanical engineering', models.CharField(blank=True, max_length=1, null=True)),
                ('environmnetal engineering, mining and energetic', models.CharField(blank=True, max_length=1, null=True)),
                ('pharmaceutical sciences', models.CharField(blank=True, max_length=1, null=True)),
                ('medical sciences', models.CharField(blank=True, max_length=1, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('description', models.TextField(blank=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication_upload', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.upload')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]