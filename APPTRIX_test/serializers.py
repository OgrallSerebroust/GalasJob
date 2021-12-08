from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source="user.first_name")
    lastname = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    class Meta:
        model = Profile
        fields = ["avatar", "gender", "firstname", "lastname", "email"]