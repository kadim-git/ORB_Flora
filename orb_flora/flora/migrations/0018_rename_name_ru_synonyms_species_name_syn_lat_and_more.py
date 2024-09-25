# Generated by Django 4.2.15 on 2024-09-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0017_rename_source_person_location_source_info_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="species",
            old_name="name_ru_synonyms",
            new_name="name_syn_lat",
        ),
        migrations.AddField(
            model_name="species",
            name="name_syn_ru",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]