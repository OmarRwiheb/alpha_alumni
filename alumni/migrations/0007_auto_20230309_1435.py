# Generated by Django 2.2.5 on 2023-03-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0006_auto_20230309_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='photo',
            field=models.ImageField(blank=True, upload_to='./alumni/alumni_images'),
        ),
    ]