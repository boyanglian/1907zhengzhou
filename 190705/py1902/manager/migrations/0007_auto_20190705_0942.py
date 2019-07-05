# Generated by Django 2.2 on 2019-07-05 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20190704_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'ordering': ('-id',), 'verbose_name': '管理员表'},
        ),
        migrations.CreateModel(
            name='Admin_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, verbose_name='操作类型')),
                ('title', models.CharField(max_length=150, verbose_name='操作日志标题')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='操作时间')),
                ('user_agent', models.CharField(max_length=240, verbose_name='记录用户客户端信息')),
                ('referer', models.CharField(max_length=100, verbose_name='操作来源页')),
                ('ip', models.CharField(max_length=15, verbose_name='ip')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='manager.Admin', verbose_name='管理员模型的外键')),
            ],
        ),
    ]
