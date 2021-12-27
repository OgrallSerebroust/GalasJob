from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('categories/', views.categories, name="Categories"),
    path('categories/<int:category_id>/', views.currencies, name="Currencies"),
    path('categories/<int:category_id>/currency/<int:currency_id>/', views.currency, name="Currency"),
]
