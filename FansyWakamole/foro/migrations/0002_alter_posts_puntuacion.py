# Generated by Django 4.2.7 on 2023-11-07 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Puntuacion',
            field=models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')], default=1),
        ),
    ]