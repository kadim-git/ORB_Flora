# Generated by Django 4.2.15 on 2024-09-12 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("oka_basin", "0007_delete_speciesdistrict"),
        ("flora", "0013_alter_family_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Locations",
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
                ("coordinate_lat_n", models.FloatField()),
                ("coordinate_long_e", models.FloatField()),
                ("coordinates_exact", models.BooleanField(default=False)),
                ("observation_date", models.DateField(blank=True)),
                ("source_acronym", models.CharField(blank=True, max_length=6)),
                ("source_publication", models.TextField(blank=True)),
                ("source_inaturalist", models.URLField(blank=True, max_length=50)),
                ("source_person", models.TextField(blank=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Reliability",
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
                (
                    "reliability",
                    models.IntegerField(
                        choices=[
                            (0, "не отмечен"),
                            (1, "наблюдение до 1961г"),
                            (2, "наблюдение после 1960г"),
                            (3, "Гербарий до 1961г"),
                            (4, "Гербарий до 1961г и наблюдение после 1960г"),
                            (5, "Гербарий после 1960г"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "district_id",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="oka_basin.district",
                        verbose_name="district name",
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="family",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="genus",
            options={"ordering": ["name"]},
        ),
        migrations.RenameField(
            model_name="species",
            old_name="name",
            new_name="name_short",
        ),
        migrations.RemoveField(
            model_name="species",
            name="slug",
        ),
        migrations.AddField(
            model_name="species",
            name="distribution",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="species",
            name="habitat",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="species",
            name="name_ru_synonyms",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name="SpeciesDistrict",
        ),
        migrations.AddField(
            model_name="reliability",
            name="species_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="flora.species",
                verbose_name="species name",
            ),
        ),
        migrations.AddField(
            model_name="locations",
            name="species_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="flora.species",
                verbose_name="species name",
            ),
        ),
    ]