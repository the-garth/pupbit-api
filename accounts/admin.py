from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'user_id',
                    'first_name', 'last_name', 'is_staff']
    readonly_fields = ('user_id',)
    fieldsets = (
        (None, {
            'fields': ('email', 'is_staff', 'is_active',
                       'username', 'password', 'user_id', 'first_name', 'last_name', 'profile_picture',
                       'phone_number', 'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country'
                       ),
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'username', 'password1', 'password2', 'is_staff', 'first_name', 'last_name', 'profile_picture',
                'phone_number', 'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country'
            ),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
