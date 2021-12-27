from django.shortcuts import render
from .models import Category, Currency, CurrencyImg


def index(request):
    return render(request, "galas_job_index.html")


def categories(request):
    categories = Category.objects.all()
    return render(request, "galas_job_categories.html", {"categories": categories})


def currencies(request, category_id):
    category = Category.objects.get(id=category_id)
    currencies = Currency.objects.filter(category=category)
    return render(request, "currencies.html", {'category': category, "currencies": currencies})


def currency(request, category_id, currency_id):
    currency = Currency.objects.get(id=currency_id)
    imgs = CurrencyImg.objects.filter(currency=currency)
    return render(request, "currency.html", {"currency": currency, "imgs": imgs})
