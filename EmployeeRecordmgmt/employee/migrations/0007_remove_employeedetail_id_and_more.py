# Generated by Django 4.2.4 on 2023-09-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_rename_joinindate_employeedetail_joiningdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetail',
            name='id',
        ),
        migrations.AlterField(
            model_name='employeedetail',
            name='empcode',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]