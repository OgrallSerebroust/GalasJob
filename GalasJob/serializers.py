from rest_framework import serializers
from .models import Category, Currency, CurrencyImg


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["name", "price", "category"]


class CurrencyIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyImg
        fields = ["image", "currency"]
