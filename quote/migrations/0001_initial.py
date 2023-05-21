# Generated by Django 4.2.1 on 2023-05-21 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=30, null=True)),
                ('movie_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('image_path', models.CharField(max_length=500, null=True)),
                ('created_time', models.DateField(auto_now_add=True)),
                ('updated_time', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quote',
                'verbose_name_plural': 'Quotes',
                'db_table': 'quote',
                'managed': True,
            },
        ),
    ]
