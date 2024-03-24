# Generated by Django 4.2.11 on 2024-03-20 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='importer',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='importer',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]