# Generated by Django 4.2.15 on 2024-09-05 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("oka_basin", "0005_alter_district_description_alter_district_slug_and_more"),
    ]

    operations = [
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
                ("species1", models.CharField(default="Sp1", max_length=10)),
                ("species2", models.CharField(default="Sp2", max_length=10)),
                (
                    "district_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="oka_basin.district",
                        verbose_name="district_name",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="SpecDistr",
        ),
    ]
