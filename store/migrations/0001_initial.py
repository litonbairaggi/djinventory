# Generated by Django 3.1.7 on 2021-05-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('customer_email', models.EmailField(max_length=64, unique=True)),
                ('customer_phone', models.CharField(max_length=17, unique=True)),
                ('customer_address', models.CharField(max_length=120)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('product_code', models.CharField(max_length=32)),
                ('bying_price', models.PositiveIntegerField(default=0)),
                ('selling_price', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('company_name', models.CharField(max_length=120, unique=True)),
                ('supplier_email', models.EmailField(max_length=64)),
                ('supplier_phone', models.CharField(max_length=120, unique=True)),
                ('supplier_address', models.CharField(max_length=120)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
