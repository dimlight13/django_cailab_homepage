# Generated by Django 3.2.16 on 2022-12-14 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cailab', '0018_news_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(default=str, max_length=300, verbose_name='제목'),
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='news')),
                ('news', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cailab.news')),
            ],
        ),
    ]
