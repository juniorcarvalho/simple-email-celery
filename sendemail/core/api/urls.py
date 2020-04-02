from django.conf.urls import url, include
from rest_framework import routers

from .views import EmailViewSet

router = routers.DefaultRouter()
router.register(r'email', EmailViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
