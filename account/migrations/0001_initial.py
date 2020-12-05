# Generated by Django 3.1.4 on 2020-12-05 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=256, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school.department', verbose_name='院系')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school', verbose_name='学校')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'ordering': ['-c_time'],
            },
        ),
    ]
