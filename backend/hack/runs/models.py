from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Person(models.Model):
    time_of_reaction = models.DecimalField(
        max_digits=3,
        decimal_places=2, #знаки после запятой
        validators=[
            MinValueValidator(0.1),     # ПРОВЕРКА ЗНАЧЕНИЙ
            MaxValueValidator(0.31),
        ],
    )
    acceleration = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.1),
        ],
    )
    max_speed = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(5.0),
            MaxValueValidator(15.1),
        ],
    )
    coef = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(-5.0),
            MaxValueValidator(0.1),
        ],
    )

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['id']

    def clean(self):
        max_objects = 6
        if Person.objects.count() >= max_objects and not self.pk:
            raise ValidationError('Достигнут лимит объектов, 6')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Человек №{self.pk}'


class Result(models.Model):
    person = models.OneToOneField(
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
    