from django.db import models
from django.core.validators import MinValueValidator

from products.constants import (
    MAX_LENGTH_FOR_STR,
    MAX_LENGTH_NAME,
    MAX_DIGITS,
    MAX_DECIMAL_PLACES,
    MIN_VALUE_PRICE
)


class Product(models.Model):
    """Модель списка продуктов."""

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=False,
        unique=True,
    )
    description = models.TextField(
        blank=True,
    )
    price = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=MAX_DECIMAL_PLACES,
        validators=(
            MinValueValidator(
                MIN_VALUE_PRICE
            ),
        )
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        """Возвращает строковое представление объекта пользователя."""
        return self.name[:MAX_LENGTH_FOR_STR]
