# Generated by Django 4.0.4 on 2022-06-01 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_hero_powers_villain_comic'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='author',
            field=models.TextField(default='not entered', max_length=100),
        ),
        migrations.AddField(
            model_name='comic',
            name='img',
            field=models.CharField(default='https://cdn.europosters.eu/image/1300/posters/dc-comics-rebirth-i80856.jpg', max_length=500),
        ),
        migrations.AddField(
            model_name='comic',
            name='year',
            field=models.CharField(default='TBD', max_length=20),
        )
    ]
