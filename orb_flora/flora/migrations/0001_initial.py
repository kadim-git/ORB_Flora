# Generated by Django 4.2.15 on 2024-09-05 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Species",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("index", models.IntegerField(verbose_name="index Majevsky")),
                ("name", models.CharField(max_length=30, unique=True)),
                ("name_full", models.CharField(max_length=50, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("slug", models.SlugField(verbose_name="Name in English")),
            ],
        ),
        migrations.CreateModel(
            name="SpeciesDistrict",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dist1", models.CharField(default="Sp1", max_length=10)),
                ("dist2", models.CharField(default="Sp2", max_length=10)),
                ("status", models.IntegerField()),
                (
                    "species_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flora.species",
                        verbose_name="species name",
                    ),
                ),
            ],
        ),
    ]
