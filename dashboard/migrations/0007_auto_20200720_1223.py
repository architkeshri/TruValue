# Generated by Django 3.0.7 on 2020-07-20 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200720_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonemodels',
            old_name='brand_name',
            new_name='brand',
        ),
    ]
