from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('categories/', views.categories, name="Categories"),
]
