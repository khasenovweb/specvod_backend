from django.db import models



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