from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Административный класс для модели Product."""

    list_display = (
        'name',
        'description',
        'price'
    )
