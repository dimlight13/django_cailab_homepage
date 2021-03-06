# Generated by Django 3.2.11 on 2022-03-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cailab', '0015_auto_20220301_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='institue',
        ),
        migrations.AddField(
            model_name='projects',
            name='host_institute',
            field=models.CharField(default=str, max_length=40, verbose_name='주관기관'),
        ),
        migrations.AddField(
            model_name='projects',
            name='support_department',
            field=models.CharField(default=str, max_length=40, null=True, verbose_name='주관부서'),
        ),
        migrations.AddField(
            model_name='projects',
            name='support_institue',
            field=models.CharField(default=str, max_length=40, verbose_name='지원기관'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='content',
            field=models.TextField(verbose_name='프로젝트 요약'),
        ),
    ]
