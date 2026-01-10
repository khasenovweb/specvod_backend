from django.db import models
from django_ckeditor_5.fields import CKEditor5Field




class Preim(models.Model):
    """ Преимущество """
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    desc = models.TextField(verbose_name="Описание")
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"
        ordering = [
            'order'
        ]


class Employee(models.Model):
    """ Сотрудник """
    fio = models.CharField(verbose_name="ФИО", max_length=255)
    role = models.CharField(verbose_name="Должность", max_length=255)
    img = models.ImageField(verbose_name="Фото", upload_to="employee/", null=True, blank=True)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = [
            'order'
        ]

        
class Partner(models.Model):
    """ Партнер """
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    img = models.ImageField(verbose_name="Фото", upload_to="employee/", null=True, blank=True)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
        ordering = [
            'order'
        ]

        
class Review(models.Model):
    """ Отзыв """
    source = models.ForeignKey("ReviewSource", verbose_name="Источник", on_delete=models.CASCADE)
    rating = models.FloatField(verbose_name="Оценка")
    user_name = models.CharField(verbose_name="Имя пользователя", max_length=255)
    date = models.DateField(verbose_name="Дата", auto_now=False, auto_now_add=False)
    text = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = [
            'date'
        ]

        
class ReviewSource(models.Model):
    """ Источник отзыва """
    name = models.CharField(verbose_name="Название", max_length=255)
    img = models.ImageField(verbose_name="Фото", upload_to="reviews/sources/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Источник отзыва"
        verbose_name_plural = "Источники отзыва"

        
        
class Faq(models.Model):
    """ FAQ """
    question = models.CharField(verbose_name="Вопрос", max_length=255)
    answer = CKEditor5Field(verbose_name="Ответ", null=True, blank=True)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQS"
        ordering = [
            'order'
        ]

        
class Number(models.Model):
    """ Цифра """
    value = models.CharField(verbose_name="Значение", max_length=255)
    desc = models.CharField(verbose_name="Описание", max_length=255)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.value + " " + self.desc

    class Meta:
        verbose_name = "Цифра"
        verbose_name_plural = "Цифры"
        ordering = [
            'order'
        ]

        
class Sertificate(models.Model):
    """ Сертификат """
    name = models.CharField(verbose_name="Название", max_length=255)
    img = models.ImageField(verbose_name="Фото", upload_to="sertificates/")
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
        ordering = [
            'order'
        ]

        
class Quiz(models.Model):
    """ Квиз """
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    code = models.TextField(verbose_name="Код подключения")
    btn_link = models.CharField(verbose_name="Ссылка для кнопки", max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Квиз"
        verbose_name_plural = "Квизы"
        

class Promotion(models.Model):
    """ Акция """
    name = models.CharField(verbose_name="Название", max_length=255)
    desc = models.TextField(verbose_name="Описание")
    img = models.ImageField(verbose_name="Изображение", upload_to="promotions/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

        
        
class PricePosition(models.Model):
    """ Позиция прайса """
    name = models.CharField(verbose_name="Название", max_length=255)
    price = models.CharField(verbose_name="Цена", max_length=255)
    img = models.ImageField(verbose_name="Изображение", upload_to="price_positions/", null=True, blank=True)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Позиция прайса"
        verbose_name_plural = "Позиции прайса"
        ordering = [
            'order'
        ]

        
class Method(models.Model):
    """ Способ бурения """
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    desc = models.TextField(verbose_name="Описание")
    img = models.ImageField(verbose_name="Изображение", upload_to="methods/")
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Способ бурения"
        verbose_name_plural = "Способы бурения"
        ordering = [
            'order'
        ]

        
class Technic(models.Model):
    """ Техника """
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    desc = models.TextField(verbose_name="Описание")
    img = models.ImageField(verbose_name="Изображение", upload_to="methods/")
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Техника"
        verbose_name_plural = "Техника"
        ordering = [
            'order'
        ]

        
class Etap(models.Model):
    """ Этап """
    name = models.CharField(verbose_name="Название", max_length=255)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Этап"
        verbose_name_plural = "Этапы"
        ordering = [
            'order'
        ]

        
class HomePage(models.Model):
    """ Главная страница """
    seo_title = models.CharField(verbose_name="SEO title", max_length=255, null=True, blank=True)
    seo_desc = models.TextField(verbose_name="SEO desc", null=True, blank=True)

    hero_title = models.CharField(verbose_name="Заголовок (первый экран)", max_length=255)
    hero_desc = models.TextField(verbose_name="Описание (первый экран)", null=True, blank=True)
    hero_bg_img = models.ImageField(verbose_name="Фоновая картинка (первый экран", upload_to="services/hero/", null=True, blank=True)
    hero_numbers = models.ManyToManyField("Number", verbose_name="Цифры (первый экран)", blank=True, related_name="homapage_hero_numbers")

    preims = models.ManyToManyField("Preim", verbose_name="Преимущества", blank=True)

    about_company_title = models.CharField(verbose_name="Заголовок (о компании)", max_length=255, null=True, blank=True)
    about_company_text = models.TextField(verbose_name="Текст (о компании)", null=True, blank=True)
    about_company_img = models.ImageField(verbose_name="Изображение (о компании)", upload_to="about_company/", null=True, blank=True)
    about_company_numbers = models.ManyToManyField("Number", verbose_name="Цифры (о компании)", blank=True, related_name="homapage_about_company_numbers")

    history_title = models.CharField(verbose_name="Заголовок (история компании)", max_length=255, null=True, blank=True)
    history_desc = models.TextField(verbose_name="Описание (история компании)", null=True, blank=True)
    history_etaps = models.ManyToManyField("HistoryEtap", verbose_name="Этапы истории", blank=True)

    services_title = models.CharField(verbose_name="Заголовок (услуги)", max_length=255, null=True, blank=True)
    services_desc = models.TextField(verbose_name="Описание (услуги)", null=True, blank=True)

    faqs = models.ManyToManyField("Faq", verbose_name="FAQS", blank=True)


    def __str__(self):
        return self.hero_title

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

        

class HistoryEtap(models.Model):
    """ Этап истории """
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    desc = models.TextField(verbose_name="Описание")
    img = models.ImageField(verbose_name="Изображение", upload_to="history_etaps/")
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Этап истории"
        verbose_name_plural = "Этапы истории"
        ordering = [
            'order'
        ]