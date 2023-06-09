# Generated by Django 4.2.1 on 2023-06-07 06:58

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmographie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acteur',
            name='photos',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='date',
            field=models.DateField(default=datetime.date(2023, 6, 7)),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='note',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
