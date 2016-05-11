from django.conf.urls import url, include

from rest_framework import routers

from .views import LocationViewSet, NightViewSet, MeasurementViewSet

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet, base_name='location')
router.register(r'nights', NightViewSet, base_name='night')
router.register(r'measurements', MeasurementViewSet, base_name='measurement')

urlpatterns = [
    url(r'^', include(router.urls)),
]
