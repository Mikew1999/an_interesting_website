# Generated by Django 3.2.7 on 2021-11-19 08:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=3000), default=[], size=None),
        ),
    ]
