# Generated by Django 4.2.15 on 2024-09-06 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0005_alter_species_name_full_alter_species_name_ru"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="species",
            name="name_ru",
        ),
    ]
