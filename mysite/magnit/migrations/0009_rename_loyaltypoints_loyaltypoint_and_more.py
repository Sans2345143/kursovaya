# Generated by Django 5.0.6 on 2024-06-20 12:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magnit', '0008_remove_customuser_loyalty_level_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoyaltyPoints',
            new_name='LoyaltyPoint',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='loyalty_points',
            new_name='loyalty_point',
        ),
        migrations.RenameField(
            model_name='loyaltylevel',
            old_name='required_points',
            new_name='minimum_points',
        ),
        migrations.AddField(
            model_name='loyaltylevel',
            name='point_percentage',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loyaltylevel',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magnit.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
