# Generated by Django 4.0.5 on 2022-07-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotWater_app', '0005_hotsprings_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotsprings',
            name='insta',
            field=models.TextField(blank=True, null=True),
        ),
    ]
