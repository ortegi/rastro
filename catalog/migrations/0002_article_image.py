# Generated by Django 5.1.2 on 2024-10-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.CharField(default='default_image.jpg', max_length=100),
        ),
    ]
