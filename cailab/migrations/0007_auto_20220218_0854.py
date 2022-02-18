# Generated by Django 3.2.11 on 2022-02-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cailab', '0006_auto_20220218_0827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biography',
            old_name='interest_se',
            new_name='interest_second',
        ),
        migrations.AddField(
            model_name='biography',
            name='link_address',
            field=models.URLField(default=str),
        ),
        migrations.AlterField(
            model_name='biography',
            name='interest_third',
            field=models.CharField(blank=True, default=str, max_length=50),
        ),
    ]
