from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PetListAsAdmin, PetViewAsOwner, PetViewDetailAsOwnerOrAdmin, PetDetail

router = SimpleRouter()
router.register(r'detail', PetDetail,
                basename='pet-detail')
router.register(r'admin/pets', PetListAsAdmin, basename='admin-pet')
router.register(r'owner/pets', PetViewAsOwner, basename='owner-pet')
router.register(r'owner/pets/detail', PetViewDetailAsOwnerOrAdmin,
                basename='owner-pet-detail')

urlpatterns = [
    *router.urls,
]
