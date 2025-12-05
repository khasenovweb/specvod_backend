from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from main.models import *



class Service(MPTTModel):
    """ Услуга """
    seo_title = models.CharField(verbose_name="SEO title", max_length=255, null=True, blank=True)
    seo_desc = models.TextField(verbose_name="SEO desc", max_length=255, null=True, blank=True)
    name = models.CharField(verbose_name="Название", max_length=255)
    slug = models.SlugField(verbose_name="SLUG", unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    price = models.CharField(verbose_name="Цена", max_length=255, null=True, blank=True)

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

    properties = models.ManyToManyField("Property", verbose_name="Характеристики", blank=True)

    price_positions = models.ManyToManyField("main.PricePosition", verbose_name="Позиции прайса", blank=True)

    show_calc = models.BooleanField(verbose_name="Показывать калькулятор расчета стоимости бурения и обустройства скважины", default=False)
    show_calc_2 = models.BooleanField(verbose_name="Показывать калькулятор расчета стоимости канализационной насосной станции", default=False)

    methods_title = models.CharField(verbose_name="Заголовок (способы бурения)", max_length=255, null=True, blank=True)
    methods_desc = models.TextField(verbose_name="Описание (способы бурения)", null=True, blank=True)
    methods_subtitle = models.CharField(verbose_name="Подзаголовок (способы бурения)", max_length=255, null=True, blank=True)
    methods_bg = models.ImageField(verbose_name="Фоновое изображение (способы бурения)", upload_to="methods/bg/", null=True, blank=True)
    methods = models.ManyToManyField("main.Method", verbose_name="Способы бурения", blank=True)

    technics_title = models.CharField(verbose_name="Заголовок (техника)", max_length=255, null=True, blank=True)
    technics = models.ManyToManyField("main.Technic", verbose_name="Техника", blank=True)

    etaps_title = models.CharField(verbose_name="Заголовок (этапы)", max_length=255, null=True, blank=True)
    etaps_subtitle = models.CharField(verbose_name="Подзаголовок (этапы)", max_length=255, null=True, blank=True)
    etaps_img = models.ImageField(verbose_name="Изображение (этапы)", upload_to="etaps/", null=True, blank=True)
    etaps = models.ManyToManyField("main.Etap", verbose_name="Этапы", blank=True)

    # здесь должны быть работы
    
    reviews = models.ManyToManyField("main.Review", verbose_name="Отзывы", blank=True)

    faqs = models.ManyToManyField("main.Faq", verbose_name="FAQS", blank=True)

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


class Property(models.Model):
    """ Характеристика """
    name = models.CharField(verbose_name="Название", max_length=255)
    value = models.CharField(verbose_name="Значение", max_length=255)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.name + ": " + self.value

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"
        ordering = [
            'order'
        ]