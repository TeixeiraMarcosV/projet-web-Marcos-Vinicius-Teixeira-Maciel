# Generated by Django 4.2 on 2023-04-16 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualisation', '0002_alter_equipe_non_entraineur_delete_entraineur'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournoi',
            name='liste_equipes',
            field=models.ManyToManyField(to='visualisation.equipe'),
        ),
    ]
