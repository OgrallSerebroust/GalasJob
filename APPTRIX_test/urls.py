from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.apptrix_test_main),
    path('api/clients/create/', include('django.contrib.auth.urls')),
    path('api/list', views.ProfileList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)