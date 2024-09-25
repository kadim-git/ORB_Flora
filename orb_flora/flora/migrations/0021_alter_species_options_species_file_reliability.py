# Generated by Django 4.2.15 on 2024-09-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0020_remove_species_is_completed_alter_family_description_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="species",
            options={"ordering": ["name_short"]},
        ),
        migrations.AddField(
            model_name="species",
            name="file_reliability",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]
