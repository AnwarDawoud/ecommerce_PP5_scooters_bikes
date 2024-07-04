# Generated by Django 3.2.23 on 2024-07-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0023_auto_20240703_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='order',
            name='discount_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]