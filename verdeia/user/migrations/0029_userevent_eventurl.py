# Generated by Django 5.0.2 on 2024-08-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_remove_userdata_volunteer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userevent',
            name='eventurl',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
