# Generated by Django 3.2.13 on 2022-08-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_alter_program_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/featured-job/img-04.png', null=True, upload_to=''),
        ),
    ]
