# Generated by Django 4.2 on 2023-04-17 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0004_remove_poule_liste_equipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='poule',
            name='liste_equipe',
            field=models.ManyToManyField(to='visualisation.equipe'),
        ),
    ]