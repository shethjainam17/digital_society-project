# Generated by Django 4.0.2 on 2022-02-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_user_created_at_remove_user_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(default='media/images/socity.jpg', upload_to='media/images/'),
        ),
    ]
