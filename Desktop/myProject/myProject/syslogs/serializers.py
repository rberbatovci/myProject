from rest_framework import serializers
from syslogs.models import Syslog

# Syslog Serializer
class SyslogSerializer(serializers.ModelSerializer):
	class Meta:
		model = Syslog
		fields = '__all__'
