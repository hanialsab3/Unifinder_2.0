# Generated by Django 3.2.13 on 2022-08-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_university_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='Deadline',
        ),
        migrations.AddField(
            model_name='program',
            name='Deadline',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
