from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
    time_of_reaction = models.DecimalField(
        max_digits=3,
        decimal_places=2, #знаки после запятой
        validators=[
            MinValueValidator(0.1),     # ПРОВЕРКА ЗНАЧЕНИЙ
            MaxValueValidator(0.3),
        ],
    )
    acceleration = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0),
        ],
    )
    max_speed = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(5.0),
            MaxValueValidator(15.0),
        ],
    )
    coef = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(-5.0),
            MaxValueValidator(0.0),
        ],
    )

