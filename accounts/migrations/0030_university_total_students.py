# Generated by Django 3.2.13 on 2022-08-07 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20220805_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='total_students',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
