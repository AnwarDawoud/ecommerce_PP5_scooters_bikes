# Generated by Django 3.2.23 on 2024-07-01 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0016_alter_order_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='discountcode',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
