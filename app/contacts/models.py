from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



class Office(models.Model):
    """ Офис """
    name = models.CharField(verbose_name="Название", max_length=255)
    working_house = models.CharField(verbose_name="Рабочие часы", max_length=255)
    adress = models.TextField(verbose_name="Адрес")
    phone = models.CharField(verbose_name="Телефон", max_length=255)
    email = models.CharField(verbose_name="E-mail", max_length=255)
    map_mapker = models.CharField(verbose_name="Метка на карте", max_length=255)
    img = models.ImageField(verbose_name="Фото", upload_to="contacts/offices/", null=True, blank=True)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Офис"
        verbose_name_plural = "Офисы"
        ordering = [
            'order'
        ]


class Employee(models.Model):
    """ Сотрудники """
    role = models.CharField(verbose_name="Должность", max_length=255)
    fio = models.CharField(verbose_name="ФИО", max_length=255)
    phone = models.CharField(verbose_name="Телефон", max_length=255)
    email = models.CharField(verbose_name="E-mail", max_length=255)
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = [
            'order'
        ]

        
class File(models.Model):
    """ Файл """
    name = models.CharField(verbose_name="Название", max_length=255)
    file = models.FileField(verbose_name="Файл", upload_to="contacts/files/")
    order = models.IntegerField(verbose_name="Порядок сортировки", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
        ordering = [
            'order'
        ]


class Contacts(models.Model):
    """ Контакты """
    adress = models.TextField(verbose_name="Адрес")
    adress_link = models.URLField(verbose_name="Ссылка проложить маршрут")
    phone_1 = models.CharField(verbose_name="Телефон 1", max_length=255)
    phone_2 = models.CharField(verbose_name="Телефон 2", max_length=255)
    vk = models.CharField(verbose_name="Вконтакте", max_length=255)
    whatsapp = models.CharField(verbose_name="WhatsApp", max_length=255)
    conpany_name = models.TextField(verbose_name="Название огранизации")
    inn_kpp = models.CharField(verbose_name="ИНН/КПП", max_length=255)
    ogrn = models.CharField(verbose_name="ОГРН", max_length=255)
    policy_text_title = models.CharField(verbose_name="Заголовок политики конфиденциальности", max_length=255, null=True, blank=True)
    policy_text = CKEditor5Field(verbose_name="Текст политики конфиденциальности", null=True, blank=True)
    cookie_text_title = models.CharField(verbose_name="Заголовок cookie", max_length=255, null=True, blank=True)
    cookie_text = CKEditor5Field(verbose_name="Текст cookie", null=True, blank=True)

    def __str__(self):
        return self.adress

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"