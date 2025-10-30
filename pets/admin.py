from django.contrib import admin

# Register your models here.
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet_id', 'owner', 'species',
                    'breed', 'vaccination_status')
    search_fields = ('name', 'breed', 'owner__username')
    list_filter = ('species', 'vaccination_status', 'speyed_neutered')
    readonly_fields = ('pet_id', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            "fields": (
                "pet_id", "name", "owner", "photo", "species", "breed",
                "sex", "date_of_birth", "color", "microchip_id"
            ),
        }),
        ("Health", {
            "fields": (
                "weight_kg", "speyed_neutered", "vaccination_status",
                "last_vaccination_date"
            ),
        }),
        ("Vet", {
            "fields": (
                "vet_name", "vet_contact_number", "vet_address_1",
                "vet_address_2", "vet_city", "vet_state",
                "vet_postal_code", "vet_country"
            ),
        }),
        ("Tracking", {"fields": ("last_known_location",)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
