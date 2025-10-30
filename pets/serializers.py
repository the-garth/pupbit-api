from rest_framework import serializers

from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetSerializerAsAdmin(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'


class PetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'pet_id', 'photo', 'name', 'date_of_birth', 'breed',
                  'owner', 'is_lost', 'last_known_location', 'vet_name',
                  'vet_contact_number', 'vaccination_status')
