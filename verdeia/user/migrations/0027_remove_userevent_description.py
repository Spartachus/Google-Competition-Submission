# Generated by Django 5.0.2 on 2024-08-07 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_rename_user_event_userevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userevent',
            name='description',
        ),
    ]
