# Generated by Django 2.2.5 on 2019-11-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20191120_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
