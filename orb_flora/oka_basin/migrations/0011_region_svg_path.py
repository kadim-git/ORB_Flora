# Generated by Django 4.2.15 on 2024-10-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oka_basin", "0010_alter_region_description_alter_region_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="region",
            name="svg_path",
            field=models.TextField(
                blank=True, default="", verbose_name="Границы области, SVG path"
            ),
        ),
    ]
