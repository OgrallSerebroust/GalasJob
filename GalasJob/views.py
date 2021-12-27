from django.shortcuts import render
from .models import Category


def index(request):
    return render(request, "galas_job_index.html")


def categories(request):
    categories = Category.objects.all()
    return render(request, "galas_job_categories.html", {"categories": categories})


def products(request):
    return render(request, "galas_job_index.html")
