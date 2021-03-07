from django.db import models


class Movie(models.Model):
    name = models.CharField(
        verbose_name='Nombre de la pelicula', max_length=50)

    class Meta:
        app_label = 'movies'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name
