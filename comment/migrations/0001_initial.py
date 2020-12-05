# Generated by Django 3.1.4 on 2020-12-05 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('zan', models.IntegerField(verbose_name='赞')),
                ('cai', models.IntegerField(verbose_name='踩')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='课程')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user', verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论表',
                'verbose_name_plural': '评论表',
                'ordering': ['-c_time'],
            },
        ),
    ]
