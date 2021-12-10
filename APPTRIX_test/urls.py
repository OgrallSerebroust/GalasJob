from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.apptrix_test_main),
    path('api/clients/create/', views.apptrix_registration, name='registration'),
    path('api/clients/create/confirm', views.CreateClientAPIView.as_view(), name='reg_confirm'),
    path('api/list', views.ProfileList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)