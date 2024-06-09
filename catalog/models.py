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
    image = models.ImageField(upload_to="product/photo/", verbose_name="изображение", **NULLABLE)
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
    view_counter = models.IntegerField(verbose_name="количество просмотров", help_text="Количество просмотров", default=0)
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'

class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="продукт",
        related_name="versions",)
    version_number = models.IntegerField(verbose_name="номер версии")
    version_name = models.CharField(max_length=100, verbose_name="название версии")
    is_active = models.BooleanField(default=False, verbose_name="текущая версия")

    def __str__(self):
        return f"{self.product}: {self.version_name}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = 'Версии'