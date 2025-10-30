from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Pet
from .permissions import IsOwnerOrReadOnly
from .serializers import PetSerializer, PetSerializerAsAdmin, PetDetailSerializer

# Create your views here.


class PetDetail(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Pet.objects.all()
    serializer_class = PetDetailSerializer


class PetListAsAdmin(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Pet.objects.all()
    serializer_class = PetSerializerAsAdmin


class PetViewAsOwner(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetViewDetailAsOwnerOrAdmin(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        # Restrict pets to those owned by the authenticated user
        return self.queryset.filter(owner=self.request.user | IsAdminUser())
