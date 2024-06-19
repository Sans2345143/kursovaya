# Generated by Django 5.0.6 on 2024-06-19 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magnit', '0006_customuser_loyalty_level_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasehistory',
            old_name='amount_spent',
            new_name='loyalty_points',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='user',
        ),
        migrations.AlterField(
            model_name='purchasehistory',
            name='product',
            field=models.CharField(max_length=255),
        ),
    ]
