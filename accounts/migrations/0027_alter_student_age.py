# Generated by Django 3.2.13 on 2022-08-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_student_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]