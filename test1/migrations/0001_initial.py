# Generated by Django 5.0 on 2024-01-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=30, unique=True)),
                ('product_name', models.CharField(max_length=30)),
                ('product_description', models.CharField(max_length=400)),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
    ]
