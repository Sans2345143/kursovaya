# Generated by Django 5.0.6 on 2024-06-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magnit', '0003_alter_customuser_options_customuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='unique_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
