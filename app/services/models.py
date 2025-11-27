from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from main.models import *

# Create your models here.



class Service(MPTTModel):
    """ Услуга """
    seo_title = models.CharField(verbose_name="SEO title", max_length=255, null=True, blank=True)
    seo_desc = models.TextField(verbose_name="SEO desc", max_length=255, null=True, blank=True)
    name = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="SLUG", unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    hero_title = models.CharField(verbose_name="Заголовок (первый экран)", max_length=255, null=True, blank=True)
    hero_desc = models.TextField(verbose_name="Описание (первый экран)", max_length=255, null=True, blank=True)
    hero_bg_img = models.ImageField(verbose_name="Фоновая картинка (первый экран", upload_to="services/hero/", null=True, blank=True)
    hero_numbers = models.ManyToManyField("main.Number", verbose_name="Цифры (первый экран)", blank=True)

    preims = models.ManyToManyField("main.Preim", verbose_name="Преимущества", blank=True)

    sertificates = models.ManyToManyField("main.Sertificate", verbose_name="Сертификаты", blank=True)

    quiz = models.ForeignKey("main.Quiz", verbose_name="Квиз", null=True, blank=True, on_delete=models.SET_NULL)

    textblock_text = CKEditor5Field(verbose_name="Текст (текстовый блок)", null=True, blank=True)
    textblock_img = models.ImageField(verbose_name="Изображение (текстовый блок)", upload_to="services/textblock/", null=True, blank=True)

    promotions = models.ManyToManyField("main.Promotion", verbose_name="Акции", blank=True)

    childrens_title = models.CharField(verbose_name="Заголовок дочерних услуг", max_length=255, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_slugs(self):
        parents = self.get_ancestors()
        tree = [el.slug for el in parents]
        slugs = "/".join(tree)
        return slugs

    def get_url(self):
        parents = self.get_ancestors()
        tree = [el.slug for el in parents]
        tree.append(self.slug)
        slugs = "/" + "/".join(tree) + "/"
        return slugs

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        # ordering = [
        #     'order'
        # ]
