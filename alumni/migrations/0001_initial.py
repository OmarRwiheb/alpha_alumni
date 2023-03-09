# Generated by Django 3.2.18 on 2023-03-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('joined_aiesec_at', models.DateField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
