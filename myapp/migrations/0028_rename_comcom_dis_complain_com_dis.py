# Generated by Django 4.0.4 on 2022-04-17 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_complain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complain',
            old_name='comcom_dis',
            new_name='com_dis',
        ),
    ]
