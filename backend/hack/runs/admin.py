from django.contrib import admin
from django.http import HttpRequest
from .models import Person, Result


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'time_of_reaction', 'acceleration', 'max_speed', 'coef','color']
    list_filter = ['id']
    search_fields = ['id']
    ordering = ['id']
    

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin): #ТОТАЛЬНЫЙ ЗАПРЕТ
    readonly = [field.name for field in Result._meta.fields]

    def has_add_permission(self, request):
        return False