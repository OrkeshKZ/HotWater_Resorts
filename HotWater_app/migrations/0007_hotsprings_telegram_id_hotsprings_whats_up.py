# Generated by Django 4.0.5 on 2022-07-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotWater_app', '0006_alter_hotsprings_insta'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotsprings',
            name='Telegram_ID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='hotsprings',
            name='Whats_Up',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]