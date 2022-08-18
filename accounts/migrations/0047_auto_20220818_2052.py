# Generated by Django 3.2.13 on 2022-08-18 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_alter_application_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='email',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='cv',
            field=models.FileField(null=True, upload_to='cv/'),
        ),
    ]
