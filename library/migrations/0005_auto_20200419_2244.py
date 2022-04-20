# Generated by Django 3.0.5 on 2020-04-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_author_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(default='download.png', upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='download.png', upload_to='book_cover'),
        ),
    ]
