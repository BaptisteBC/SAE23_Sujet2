# Generated by Django 4.2.1 on 2023-06-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmographie', '0003_alter_acteur_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='affiche',
            field=models.ImageField(null=True, upload_to='filmographie/images/'),
        ),
    ]
