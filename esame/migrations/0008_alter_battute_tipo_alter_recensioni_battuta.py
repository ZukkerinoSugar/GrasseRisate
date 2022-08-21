# Generated by Django 4.1 on 2022-08-21 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esame', '0007_remove_battute_media_voti_remove_battute_numero_voti_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battute',
            name='tipo',
            field=models.CharField(choices=[('Sat', 'Satira'), ('Bar', 'Barzelletta'), ('Bhu', 'Black Humor'), ('Bsq', 'Battute Squallide')], default='bar', max_length=3),
        ),
        migrations.AlterField(
            model_name='recensioni',
            name='battuta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='battutarec', to='esame.battute'),
        ),
    ]
