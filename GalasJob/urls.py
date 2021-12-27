from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('categories/', views.categories, name="Categories"),
    path('categories/<int:category_id>/', views.currencies, name="Currencies"),
    path('categories/<int:category_id>/currency/<int:currency_id>/', views.currency, name="Currency"),
]

urlpatterns += [
    path('api/categories/', views.CategoryListCreateAPIView.as_view()),
    path('api/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/currencies/', views.CurrencyListCreateAPIView.as_view()),
    path('api/currencies/<int:pk>/', views.CurrencyRetrieveUpdateDestroyAPIView.as_view()),
    path('api/currency_images/', views.CurrencyIMGListCreateAPIView.as_view()),
    path('api/currency_images/<int:pk>/', views.CurrencyIMGRetrieveUpdateDestroyAPIView.as_view()),
]
