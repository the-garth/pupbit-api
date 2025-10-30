from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CustomUserDetail, CustomUserDetailAsAdmin, CustomUserListAsAdmin

# Using custom router to register viewsets, to show difference between viewset and generic views in Posts

router = SimpleRouter()
router.register(r'admin', CustomUserListAsAdmin, basename='customuser-admin')
router.register(r'detail', CustomUserDetailAsAdmin,
                basename='customuser-detail')
router.register(r'', CustomUserDetail, basename='customuser')

urlpatterns = [
    *router.urls,
]
