from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Person(models.Model):
    time_of_reaction = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(0.31),
        ],
        verbose_name='Время реакции'
    )
    acceleration = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.1),
        ],
        verbose_name='Ускорение'
    )
    max_speed = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(5.0),
            MaxValueValidator(15.1),
        ],
        verbose_name='Макс. скорость'
    )
    coef = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(-2.1),
            MaxValueValidator(0.1),
        ],
        verbose_name='Коэффициент'
    )
    color = models.CharField(
        max_length=16,
        verbose_name='Цвет',
        help_text='HEX-код цвета (#FFFFFF)'
    )

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
        ordering = ['id']

    def clean(self):
        max_objects = 6
        if Person.objects.count() >= max_objects and not self.pk:
            raise ValidationError('Достигнут лимит участников (6)')
        
        if not self.color.startswith('#'):
            raise ValidationError('Цвет должен быть в HEX-формате (#FFFFFF)')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Участник #{self.id}'
class Result(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.PROTECT,
        related_name='result',
        verbose_name='Человек',
    )
    
    value = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ]
    )
    
    class Meta:
        verbose_name = 'Результат',
        verbose_name_plural = 'Результаты'

    def __str__(self):
        return f'Результат {self.person.pk}: {self.value}'
    