# Generated by Django 4.0.5 on 2022-06-17 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hot_app', '0002_hotsprings_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotsprings',
            name='geoposition',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]