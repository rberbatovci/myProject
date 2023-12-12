from syslogs.models import Syslog
from rest_framework import viewsets, permissions
from .serializers import SyslogSerializer

# Syslog Viewset
class SyslogViewSet(viewsets.ModelViewSet):
	queryset = Syslog.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = SyslogSerializer
