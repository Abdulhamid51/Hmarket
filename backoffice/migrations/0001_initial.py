# Generated by Django 4.0.2 on 2022-03-04 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sold_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product')),
            ],
        ),
    ]
