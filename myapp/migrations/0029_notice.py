# Generated by Django 4.0.4 on 2022-04-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_rename_comcom_dis_complain_com_dis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_title', models.CharField(max_length=20)),
                ('dob', models.DateField(auto_now_add=True)),
                ('notice_dis', models.CharField(max_length=50)),
            ],
        ),
    ]