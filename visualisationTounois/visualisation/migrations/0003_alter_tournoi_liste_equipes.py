# Generated by Django 4.2 on 2023-04-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0002_alter_tournoi_liste_equipes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournoi',
            name='liste_equipes',
            field=models.ManyToManyField(to='visualisation.equipe'),
        ),
    ]