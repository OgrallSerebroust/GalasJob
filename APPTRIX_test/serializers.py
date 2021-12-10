from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source="user.first_name", help_text="Имя")
    lastname = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")

    class Meta:
        model = Profile
        fields = ["avatar", "gender", "firstname", "lastname", "email"]

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)