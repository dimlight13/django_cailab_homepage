# Generated by Django 3.2.11 on 2022-02-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cailab', '0003_rename_title_image_post_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('content', models.TextField()),
            ],
        ),
    ]