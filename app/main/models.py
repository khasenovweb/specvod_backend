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