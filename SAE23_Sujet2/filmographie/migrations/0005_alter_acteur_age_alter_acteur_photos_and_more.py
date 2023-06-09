# Generated by Django 4.2.1 on 2023-06-09 09:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmographie', '0004_alter_film_affiche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acteur',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='acteur',
            name='photos',
            field=models.ImageField(null=True, upload_to='filmographie/acteur/'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(default=datetime.date(2023, 6, 9)),
        ),
        migrations.AlterField(
            model_name='film',
            name='affiche',
            field=models.ImageField(null=True, upload_to='filmographie/film/'),
        ),
    ]
