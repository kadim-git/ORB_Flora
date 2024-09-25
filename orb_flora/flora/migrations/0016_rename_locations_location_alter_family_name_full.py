# Generated by Django 4.2.15 on 2024-09-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0015_alter_locations_coordinate_lat_n_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Locations",
            new_name="Location",
        ),
        migrations.AlterField(
            model_name="family",
            name="name_full",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Название полное"
            ),
        ),
    ]
