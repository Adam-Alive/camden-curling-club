# Generated by Django 4.2.13 on 2024-06-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='caption',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
