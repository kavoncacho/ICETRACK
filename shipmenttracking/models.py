from django.db import models
import uuid

class shipmentTrack (models.Model):
    class Meta:
        verbose_name = "Tracking Code"

    trackingCode = models.IntegerField(default=0)

# Create your models here.
