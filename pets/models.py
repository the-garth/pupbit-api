import uuid
from django.db import models

# Create your models here.


class Pet(models.Model):
    class VaccinationStatus(models.TextChoices):
        UP_TO_DATE = "up_to_date", "Up to date"
        DUE_SOON = "due_soon", "Due soon"
        OVERDUE = "overdue", "Overdue"
        UNKNOWN = "unknown", "Unknown"

    pet_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    species = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    breed = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    microchip_id = models.CharField(max_length=50, blank=True, null=True)
    weight_kg = models.FloatField()
    speyed_neutered = models.BooleanField(default=False)
    vaccination_status = models.CharField(
        max_length=20,
        choices=VaccinationStatus.choices,
        default=VaccinationStatus.UNKNOWN,
    )
    last_vaccination_date = models.DateField(blank=True, null=True)
    vet_name = models.CharField(max_length=100, blank=True, null=True)
    vet_contact_number = models.CharField(
        max_length=100, blank=True, null=True)
    vet_address_1 = models.TextField(blank=True, null=True)
    vet_address_2 = models.TextField(blank=True, null=True)
    vet_city = models.CharField(max_length=100, blank=True, null=True)
    vet_state = models.CharField(max_length=100, blank=True, null=True)
    vet_postal_code = models.CharField(max_length=20, blank=True, null=True)
    vet_country = models.CharField(max_length=100, blank=True, null=True)
    last_known_location = models.CharField(
        max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        'accounts.CustomUser', on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.name
