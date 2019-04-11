from django.db import models

# Create your models here.

class AirportInfo(models.Model):
    ident = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    latitude_deg = models.FloatField()
    longitude_deg = models.FloatField()
    elevation_ft = models.CharField(max_length=30, blank=True, null=True)
    continent = models.CharField(max_length=2)
    iso_country = models.CharField(max_length=2)
    iso_region = models.CharField(max_length=10)
    municipality = models.CharField(max_length=255)
    scheduled_service = models.BooleanField()
    gps_code = models.CharField(max_length=10, blank=True, null=True)
    iata_code = models.CharField(max_length=255, blank=True, null=True)
    local_code = models.CharField(max_length=255, blank=True, null=True)
    home_link = models.URLField(blank=True, null=True)
    wikipedia_link = models.URLField(blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)

    def save(self):
        self.name = self.name.capitalize()
        return super().save()

    def __str__(self):
        return self.name
