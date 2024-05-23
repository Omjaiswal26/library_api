from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'books',BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]