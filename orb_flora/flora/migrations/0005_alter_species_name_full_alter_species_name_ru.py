# Generated by Django 4.2.15 on 2024-09-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0004_alter_species_name_full_alter_species_name_ru"),
    ]

    operations = [
        migrations.AlterField(
            model_name="species",
            name="name_full",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="species",
            name="name_ru",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
