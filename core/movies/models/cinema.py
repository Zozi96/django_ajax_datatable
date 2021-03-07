from django.db import models


class Cine(models.Model):
    name = models.CharField(
        verbose_name='Nombre del cine', max_length=50)

    class Meta:
        app_label = 'movies'
        verbose_name = 'Cine'
        verbose_name_plural = 'Cines'

    def __str__(self):
        return self.name