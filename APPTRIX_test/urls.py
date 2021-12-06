from django.urls import path
from . import views

urlpatterns = [
    path('', views.apptrix_test_main),
]