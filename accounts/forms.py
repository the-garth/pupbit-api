from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture',
                  'phone_number', 'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture',
                  'phone_number', 'address_line1', 'address_line2', 'city', 'state', 'postal_code', 'country')
