from django.contrib import admin
from django.urls import path, include
from MyPage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]

urlpatterns += [
    path('apptrix_test/', include('APPTRIX_test.urls')),
    path('GalasJob/', include("GalasJob.urls")),
]
