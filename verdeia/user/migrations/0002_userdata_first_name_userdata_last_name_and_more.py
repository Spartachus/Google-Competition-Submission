# Generated by Django 5.0.2 on 2024-06-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='first_name',
            field=models.CharField(default='John', max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='last_name',
            field=models.CharField(default='Doe', max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='user_tier',
            field=models.CharField(default='Free', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_country',
            field=models.CharField(default='Verdeia Republic', max_length=50),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_email',
            field=models.CharField(default='jane.doe@email.com', max_length=50),
        ),
    ]
