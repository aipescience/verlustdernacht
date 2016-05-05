from django.conf.urls import url, include

from rest_framework import routers

from .views import MeasurementViewSet

router = routers.DefaultRouter()
router.register(r'measurements', MeasurementViewSet, base_name='measurement')

urlpatterns = [
    url(r'^', include(router.urls)),
]
