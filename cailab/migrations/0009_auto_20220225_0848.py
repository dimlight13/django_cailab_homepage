# Generated by Django 3.2.11 on 2022-02-24 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cailab', '0008_biography_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
        migrations.AlterField(
            model_name='biography',
            name='link_address',
            field=models.URLField(blank=True, default=str),
        ),
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
