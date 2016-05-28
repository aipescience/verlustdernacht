from django.conf.urls import url, include

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet, base_name='location')
router.register(r'nights', NightViewSet, base_name='night')
router.register(r'measurements', MeasurementViewSet, base_name='measurement')
router.register(r'moonpositions', MoonPositionViewSet, base_name='moonposition')

urlpatterns = [
    url(r'^', include(router.urls)),
]
