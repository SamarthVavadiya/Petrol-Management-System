# Generated by Django 4.0 on 2022-01-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_fuel_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
