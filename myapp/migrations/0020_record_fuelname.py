# Generated by Django 4.0 on 2022-01-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_record_fuelname'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='fuelname',
            field=models.CharField(default='', max_length=255),
        ),
    ]
