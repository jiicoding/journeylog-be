# Generated by Django 2.1 on 2018-12-04 04:02

from django.db import migrations, models
import journeylog.models


class Migration(migrations.Migration):

    dependencies = [
        ('journeylog', '0008_auto_20181204_0548'),
    ]

    operations = [
        migrations.AddField(
            model_name='journey',
            name='background',
            field=models.ImageField(blank=True, max_length=240, upload_to=journeylog.models.journey_background_image_path),
        ),
    ]
