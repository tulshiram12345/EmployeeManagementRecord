# Generated by Django 4.2.4 on 2023-09-05 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_rename_company1name_employeeeducation_coursegra_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='coursephsc',
            new_name='coursehsc',
        ),
    ]
