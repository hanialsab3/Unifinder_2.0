# Generated by Django 3.2.13 on 2022-08-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_alter_program_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='profile_picture',
            field=models.ImageField(blank=True, default='featured-job/img-05.png', null=True, upload_to=''),
        ),
    ]
