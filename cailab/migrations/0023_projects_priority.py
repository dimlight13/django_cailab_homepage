# Generated by Django 4.1.4 on 2023-01-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cailab', '0022_delete_category_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='우선순위'),
        ),
    ]