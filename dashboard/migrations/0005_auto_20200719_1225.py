# Generated by Django 3.0.7 on 2020-07-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200719_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodels',
            name='model_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]