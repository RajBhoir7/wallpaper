# Generated by Django 3.1.8 on 2025-03-18 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WallpaperIMg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallpaperName', models.CharField(max_length=100)),
                ('wallpaperImg', models.ImageField(upload_to='Wallpapers')),
            ],
        ),
    ]
