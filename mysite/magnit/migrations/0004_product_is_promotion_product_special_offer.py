# Generated by Django 5.0.6 on 2024-06-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magnit', '0003_remove_product_is_promotion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_promotion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='special_offer',
            field=models.BooleanField(default=False),
        ),
    ]