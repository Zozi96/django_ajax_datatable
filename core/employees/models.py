from django.db import models
from django import forms


class Employee(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=50)
    last_name = models.CharField(verbose_name='Apellido', max_length=50)
    birthday = models.DateField(verbose_name='Fecha de nacimiento', )

    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f'{self.name} {self.last_name}'

    def toJSON(self):
        item = forms.model_to_dict(self)
        return item
