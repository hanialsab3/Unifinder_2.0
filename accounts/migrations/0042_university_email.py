# Generated by Django 3.2.13 on 2022-08-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_alter_program_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='email',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
