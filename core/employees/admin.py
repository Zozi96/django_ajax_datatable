from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class Admin(admin.ModelAdmin):

    list_display = ('name', 'last_name', 'birthday', )
