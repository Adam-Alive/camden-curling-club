# Generated by Django 4.2.13 on 2024-06-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_galleryimage_caption_updated_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='caption_updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
