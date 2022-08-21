# Generated by Django 4.1 on 2022-08-20 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esame', '0005_alter_recensioni_voto'),
    ]

    operations = [
        migrations.AddField(
            model_name='battute',
            name='media_voti',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='battute',
            name='numero_voti',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='battute',
            name='somma_voti',
            field=models.IntegerField(default=0),
        ),
    ]
