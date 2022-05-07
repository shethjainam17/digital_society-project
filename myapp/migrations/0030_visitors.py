# Generated by Django 4.0.4 on 2022-04-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('flat_no', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
