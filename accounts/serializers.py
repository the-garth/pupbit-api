from rest_framework import serializers

from pets.serializers import PetSerializer
from .models import CustomUser


class CustomUserWithPetsSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ["pets",]
        read_only_fields = ("pets",)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta(CustomUserWithPetsSerializer.Meta):
        model = CustomUser
        fields = ['username', 'pets']


class CustomUserSerializerAsAdmin(serializers.ModelSerializer):
    class Meta(CustomUserWithPetsSerializer.Meta):
        model = CustomUser
        fields = ['id', 'username', 'email', 'name', 'pets', 'is_staff',
                  'is_active', 'is_superuser', 'last_login', 'date_joined']
