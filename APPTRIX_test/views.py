from django.shortcuts import render
from rest_framework import generics
from . import serializers
from .models import Profile
from django.contrib.auth.models import User


def apptrix_test_main(request):
    return render(request, "apptrix_test_main_page.html")

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer


