from rest_framework import routers
from .api import SyslogViewSet

router = routers.DefaultRouter()
router.register('api/syslogs', SyslogViewSet, 'syslogs')

urlpatterns = router.urls
