# Generated by Django 2.2 on 2019-07-05 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_auto_20190705_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='accounts',
            new_name='account',
        ),
    ]
