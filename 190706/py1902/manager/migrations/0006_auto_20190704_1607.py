# Generated by Django 2.2 on 2019-07-04 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20190704_1520'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'ordering': (['id'],), 'verbose_name': '管理员表'},
        ),
    ]
