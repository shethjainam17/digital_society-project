# Generated by Django 4.0.2 on 2022-02-16 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_watchman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchman',
            name='address',
        ),
        migrations.RemoveField(
            model_name='watchman',
            name='country',
        ),
        migrations.RemoveField(
            model_name='watchman',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='watchman',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='watchman',
            name='state',
        ),
        migrations.AddField(
            model_name='watchman',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
    ]