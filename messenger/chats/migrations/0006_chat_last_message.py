# Generated by Django 2.2.5 on 2019-11-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0005_auto_20191119_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='last_message',
            field=models.IntegerField(default=0),
        ),
    ]