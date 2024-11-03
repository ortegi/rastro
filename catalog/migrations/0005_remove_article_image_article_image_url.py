# Generated by Django 5.1.2 on 2024-11-01 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_article_image_url_article_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]