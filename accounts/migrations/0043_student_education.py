# Generated by Django 3.2.13 on 2022-08-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_university_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='education',
            field=models.TextField(null=True),
        ),
    ]