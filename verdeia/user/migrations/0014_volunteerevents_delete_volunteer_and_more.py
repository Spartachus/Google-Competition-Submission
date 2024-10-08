# Generated by Django 5.0.2 on 2024-07-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_remove_userdata_user_actualcountry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(default='Verdiea volunteer', max_length=50)),
                ('event_place', models.CharField(default='Paradiso', max_length=50)),
                ('event_id', models.CharField(default='#0013483', max_length=50)),
                ('event_description', models.CharField(default='hello world, welcome to my workplace', max_length=50)),
                ('no_of_signed', models.CharField(default='0', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Volunteer',
        ),
        migrations.AddField(
            model_name='userdata',
            name='number_events',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AddField(
            model_name='userdata',
            name='volunteer_id',
            field=models.CharField(default='#000000', max_length=50),
        ),
    ]
