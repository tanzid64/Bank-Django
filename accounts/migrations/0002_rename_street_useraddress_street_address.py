# Generated by Django 4.2.7 on 2023-12-29 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='street',
            new_name='street_address',
        ),
    ]
