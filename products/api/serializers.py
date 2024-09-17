from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продуктов.

    Используется для создания и отображения рецептов.
    """
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'Цена не может быть отрицательной'
            )
        return value