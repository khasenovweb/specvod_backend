from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from main.models import *
from services.models import *



class Work(models.Model):
    """ Работа """
    seo_title = models.CharField(verbose_name="SEO title", max_length=255, null=True, blank=True)
    seo_desc = models.TextField(verbose_name="SEO desc", max_length=255, null=True, blank=True)
    service = models.ForeignKey("services.Service", verbose_name="Услуга", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="SLUG", unique=True)
    client = models.CharField(verbose_name="Заказчик", max_length=255, null=True, blank=True)
    date = models.DateField(verbose_name="Дата", null=True, blank=True)
    img = models.ImageField(verbose_name="Изображение", upload_to="works/", null=True, blank=True)
    text = models.TextField(verbose_name="Описание", null=True, blank=True)
    numbers = models.ManyToManyField("main.Number", verbose_name="Цифры", blank=True)
    map_marker = models.CharField(verbose_name="Координаты на карте", help_text="Пример: 55.829173, 49.043343", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        slugs = "/works/" + self.slug + "/"
        return slugs

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

        
class Task(models.Model):
    """ Выполненная задача """
    work = models.ForeignKey("Work", verbose_name="Работа", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=255)
    desc = models.TextField(verbose_name="Описание")
    img = models.ImageField(verbose_name="Изображение", upload_to="works/tasks/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Выполненная задача"
        verbose_name_plural = "Выполненные задача"