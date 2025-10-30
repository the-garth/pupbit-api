from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserSerializerAsAdmin

# Create your views here.


class CustomUserDetail(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserListAsAdmin(viewsets.ModelViewSet):
    # Add appropriate permissions for admin access
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerAsAdmin


class CustomUserDetailAsAdmin(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializerAsAdmin
