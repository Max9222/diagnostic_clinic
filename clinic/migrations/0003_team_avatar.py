# Generated by Django 5.0.1 on 2024-01-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='clinic/', verbose_name='аватар'),
        ),
    ]