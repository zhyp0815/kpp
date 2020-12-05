# Generated by Django 3.1.4 on 2020-12-05 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=128)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '院系',
                'verbose_name_plural': '院系',
                'ordering': ['c_time'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=128, unique=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
                'ordering': ['c_time'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=128)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.department')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
                'ordering': ['c_time'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.school'),
        ),
    ]
