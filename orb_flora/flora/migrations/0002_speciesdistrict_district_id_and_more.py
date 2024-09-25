# Generated by Django 4.2.15 on 2024-09-05 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("oka_basin", "0007_delete_speciesdistrict"),
        ("flora", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="speciesdistrict",
            name="district_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="oka_basin.district",
                verbose_name="district name",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="speciesdistrict",
            name="status",
            field=models.IntegerField(default=0),
        ),
    ]