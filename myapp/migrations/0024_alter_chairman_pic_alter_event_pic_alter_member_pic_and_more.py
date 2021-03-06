# Generated by Django 4.0.2 on 2022-04-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='media/images/society.jpg', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pic',
            field=models.FileField(default='media/images/society.jpg', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.FileField(default='media/images/society.jpg', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pic',
            field=models.FileField(default='media/images/society.jpg', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='watchman',
            name='pic',
            field=models.FileField(default='media/images/society.jpg', upload_to='media/images/'),
        ),
    ]
