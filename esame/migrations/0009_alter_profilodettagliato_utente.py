# Generated by Django 4.1 on 2022-08-21 03:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esame', '0008_alter_battute_tipo_alter_recensioni_battuta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilodettagliato',
            name='utente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='utentedet', to=settings.AUTH_USER_MODEL),
        ),
    ]