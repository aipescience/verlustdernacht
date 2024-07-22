from django.urls import include, path

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
# router.register(r'locations', LocationViewSet.as_view(), basename='locations')
# router.register(r'nights', NightViewSet.as_view({'get': 'list'}), basename='night')
router.register(r'nights', NightViewSet, basename='night')
router.register(r'measurements', MeasurementViewSet, basename='measurement')
router.register(r'moonpositions', MoonPositionViewSet, basename='moonposition')

urlpatterns = [
    # rest api
    path('api/', include(router.urls)),
]
