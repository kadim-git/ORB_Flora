# Generated by Django 4.2.15 on 2024-10-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0021_alter_species_options_species_file_reliability"),
    ]

    operations = [
        migrations.AlterField(
            model_name="species",
            name="file_reliability",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]