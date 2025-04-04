from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_of_reaction', 'acceleration', 'max_speed', 'coef']
    list_filter = ['id']
    search_fields = ['id']
    ordering = ['id']