# Generated by Django 3.0.3 on 2022-01-25 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20220125_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='is_galery_data_type_webdev',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]