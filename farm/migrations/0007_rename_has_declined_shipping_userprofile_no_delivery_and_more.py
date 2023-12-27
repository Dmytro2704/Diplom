# Generated by Django 5.0 on 2023-12-21 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0006_remove_product_shipping_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='has_declined_shipping',
            new_name='no_delivery',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(choices=[('location1', 'Дніпро'), ('location2', 'Павлоград'), ('location3', 'Новомосковськ')], max_length=100, verbose_name='Location'),
        ),
    ]