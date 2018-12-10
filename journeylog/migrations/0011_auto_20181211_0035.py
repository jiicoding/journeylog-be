# Generated by Django 2.1 on 2018-12-10 22:35

from django.db import migrations
import journeylog.util.model


class Migration(migrations.Migration):

    dependencies = [
        ('journeylog', '0010_remove_journey_background_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalpage',
            name='disabled_modules',
            field=journeylog.util.model.FixedSeparatedValuesField(blank=True, choices=[(1, 'Description'), (2, 'Photos'), (3, 'Map')], max_length=255),
        ),
    ]
