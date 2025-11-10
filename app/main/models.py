from django.db import models




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