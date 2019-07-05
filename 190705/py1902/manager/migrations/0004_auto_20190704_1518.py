# Generated by Django 2.2 on 2019-07-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='email',
            field=models.CharField(default='', max_length=45, unique=True, verbose_name='邮箱'),
        ),
        migrations.AddField(
            model_name='admin',
            name='login_ip',
            field=models.CharField(default='', max_length=15, verbose_name='ipv4地址'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='login_num',
            field=models.PositiveIntegerField(default=0, verbose_name='登录次数'),
        ),
        migrations.AddField(
            model_name='admin',
            name='login_time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后一次登录时间'),
        ),
        migrations.AddField(
            model_name='admin',
            name='mobile',
            field=models.CharField(default='', max_length=11, unique=True, verbose_name='手机号'),
        ),
        migrations.AddField(
            model_name='admin',
            name='pwd',
            field=models.CharField(default='', max_length=32, verbose_name='密码'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admin',
            name='state',
            field=models.BooleanField(default=False, verbose_name='状态，1禁用 0正常'),
        ),
    ]