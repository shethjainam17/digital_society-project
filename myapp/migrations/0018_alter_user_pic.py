# Generated by Django 4.0.2 on 2022-02-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_rename_chairmen_chairman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.FileField(default='myapp/images/socity.jpg', upload_to='myapp/images/'),
        ),
    ]
