# Generated by Django 3.2.7 on 2021-09-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210924_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
