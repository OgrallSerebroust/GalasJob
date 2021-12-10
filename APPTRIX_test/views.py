from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from django_filters import rest_framework as filters


def apptrix_test_main(request):
    return render(request, "apptrix_test_main_page.html")


def apptrix_registration(request):
    user_form, profile_form = UserForm(), ProfileForm()
    return render(request, "apptrix_registration.html", {"user_form": user_form, "profile_form": profile_form})


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("gender", "user__first_name", "user__last_name",)


class CreateClientAPIView(generics.ListCreateAPIView):
    def post(self, request):
        serializer = serializers.ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        #return Response(user.id, status=status.HTTP_200_OK,)
    #queryset = Profile.objects.all()
    #serializer_class = serializers.ProfileSerializer
    #def perform_create(self, serializer):
        #serializer.save()
    #def post(self, request):
        #serializer = ProfileSerializer(data=request.data)
        #serializer.is_valid(raise_exeptions=True)
        #user = serializer.save()
        #return Responce(user.id, status=status.HTTP_200_OK,)
