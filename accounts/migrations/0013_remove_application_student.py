# Generated by Django 3.2.13 on 2022-05-12 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20220512_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='student',
        ),
    ]
