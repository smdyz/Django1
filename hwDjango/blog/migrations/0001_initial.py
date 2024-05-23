# Generated by Django 5.0.4 on 2024-04-16 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='заголовок')),
                ('description', models.TextField(blank=True, max_length=50, null=True, verbose_name='содержимое')),
                ('preview', models.ImageField(upload_to='', verbose_name='превью')),
                ('created_at', models.CharField(max_length=50, verbose_name='дата создания')),
                ('published', models.CharField(max_length=50, verbose_name='опубликовано')),
                ('views', models.IntegerField(verbose_name='просмотры')),
                ('slug', models.CharField(max_length=50, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]
