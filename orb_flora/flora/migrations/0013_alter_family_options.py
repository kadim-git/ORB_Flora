# Generated by Django 4.2.15 on 2024-09-08 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0012_alter_species_genus"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="family",
            options={"ordering": ["index"]},
        ),
    ]
