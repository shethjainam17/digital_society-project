# Generated by Django 4.0.4 on 2022-04-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_visitors'),
    ]

    operations = [
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.FileField(default='media/socity.jpg', upload_to='media/images/')),
                ('dob', models.DateField(auto_now_add=True)),
                ('photo_name', models.CharField(max_length=30)),
            ],
        ),
    ]
