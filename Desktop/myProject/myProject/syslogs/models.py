from django.db import models

class Syslog(models.Model):
    agent_address  = models.CharField(max_length=100)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    