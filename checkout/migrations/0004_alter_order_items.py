# Generated by Django 3.2.7 on 2021-11-19 08:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=3000), default=list, size=None),
        ),
    ]
