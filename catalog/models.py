from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование")
    description = models.TextField(
        verbose_name="описание", help_text="Введите описание"
    )

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="имя")
    description = models.TextField(
        verbose_name="описание", help_text="Введите описание"
    )
    image = models.ImageField(upload_to="images/", verbose_name="изображение", **NULLABLE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="категория",
        related_name="courses",
        **NULLABLE,
    )
    cost_of_purchase = models.IntegerField(verbose_name="цена покупки")
    created_at = models.DateField(verbose_name="дата создания", **NULLABLE)
    updated_at = models.DateField(verbose_name="дата последнего изменеия", **NULLABLE)

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'
