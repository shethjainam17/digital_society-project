# Generated by Django 4.0.2 on 2022-02-16 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_watchman_address_remove_watchman_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchman',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Chairmen',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='Watchman',
        ),
    ]