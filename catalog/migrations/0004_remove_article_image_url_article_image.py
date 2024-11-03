# Generated by Django 5.1.2 on 2024-11-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_article_image_article_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_url',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]