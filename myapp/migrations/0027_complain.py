# Generated by Django 4.0.4 on 2022-04-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_chairman_pic_alter_event_pic_alter_member_pic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_title', models.CharField(max_length=20)),
                ('comcom_dis', models.CharField(max_length=50)),
            ],
        ),
    ]