# Generated by Django 3.2.13 on 2022-08-07 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_auto_20220807_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='program',
            old_name='Deadline',
            new_name='deadline',
        ),
    ]