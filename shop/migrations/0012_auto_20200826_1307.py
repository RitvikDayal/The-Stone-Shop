# Generated by Django 3.1 on 2020-08-26 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200823_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user',
            new_name='customer',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
