# Generated by Django 4.1 on 2022-08-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esame', '0012_profilodettagliato_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilodettagliato',
            name='citta',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]