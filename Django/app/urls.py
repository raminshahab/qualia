# app/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter  # Add this line
from .views import TeamMemberViewSet

router = DefaultRouter()
router.register(r'team-members', TeamMemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]