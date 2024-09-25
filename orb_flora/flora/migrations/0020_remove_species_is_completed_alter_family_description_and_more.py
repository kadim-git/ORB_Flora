# Generated by Django 4.2.15 on 2024-09-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flora", "0019_species_work_status_alter_location_source_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="species",
            name="is_completed",
        ),
        migrations.AlterField(
            model_name="family",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="family",
            name="distribution",
            field=models.TextField(
                blank=True, null=True, verbose_name="Распространение"
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="index",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Интекс по Маевскому"
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="name",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="Название, краткое"
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="name_full",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Название полное"
            ),
        ),
        migrations.AlterField(
            model_name="family",
            name="name_ru",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Название на русском"
            ),
        ),
        migrations.AlterField(
            model_name="genus",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="genus",
            name="distribution",
            field=models.TextField(
                blank=True, null=True, verbose_name="Распространение"
            ),
        ),
        migrations.AlterField(
            model_name="genus",
            name="index",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Интекс по Маевскому"
            ),
        ),
        migrations.AlterField(
            model_name="genus",
            name="name",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="Название, краткое"
            ),
        ),
        migrations.AlterField(
            model_name="genus",
            name="name_full",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Название полное"
            ),
        ),
        migrations.AlterField(
            model_name="genus",
            name="name_ru",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Название на русском"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="species",
            name="distribution",
            field=models.TextField(
                blank=True, null=True, verbose_name="Распространение"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="habitat",
            field=models.TextField(
                blank=True, null=True, verbose_name="Среда обитания"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="index",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Интекс по Маевскому"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="name_full",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="Название полное"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="name_ru",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Название на русском"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="name_short",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="Название, краткое"
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="name_syn_lat",
            field=models.CharField(
                blank=True,
                max_length=60,
                null=True,
                verbose_name="Синоним, название научное",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="name_syn_ru",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Синоним, Название на русском",
            ),
        ),
        migrations.AlterField(
            model_name="species",
            name="work_status",
            field=models.IntegerField(
                choices=[(0, "черновик"), (1, "в работе"), (2, "завершен")],
                default=0,
                verbose_name="Рабочий статус",
            ),
        ),
    ]