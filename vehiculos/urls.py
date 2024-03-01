from rest_framework import routers

from .api import VehiculoViewSet

router = routers.DefaultRouter()

router.register('api/vehiculos', VehiculoViewSet, 'vehiculos')

urlpatterns = router.urls

