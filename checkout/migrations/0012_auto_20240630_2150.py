# Generated by Django 3.2.23 on 2024-06-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0011_auto_20240630_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='lineitem_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
