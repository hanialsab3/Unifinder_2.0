# Generated by Django 3.2.13 on 2022-08-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_student_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
