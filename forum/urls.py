from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import tPostViewSet

router = DefaultRouter()
router.register(r'posts', tPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
