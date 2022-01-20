from django.db import models


class Homepage(models.Model):
    """
    Add news
    """
    title = models.CharField(max_length=50, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Контент")
    datatime = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/",
        verbose_name="Фото",
        blank=True
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликованно?"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Категория",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "страница"
        verbose_name_plural = "страницы"
        ordering = ["-datatime"]


class Category(models.Model):
    title = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name="Наименование категории"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["pk"]
