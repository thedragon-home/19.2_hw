# Generated by Django 5.0.4 on 2024-05-02 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100, verbose_name="наименование")),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание", verbose_name="описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100, verbose_name="имя")),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание", verbose_name="описание"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/",
                        verbose_name="изображение",
                    ),
                ),
                ("cost_of_purchase", models.IntegerField(verbose_name="цена покупки")),
                ("created_at", models.DateField(verbose_name="дата создания")),
                (
                    "updated_at",
                    models.DateField(verbose_name="дата последнего изменеия"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="courses",
                        to="catalog.category",
                        verbose_name="категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]