from rest_framework import serializers
from .models import AirportInfo

class AirportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportInfo
        fields = ('name', 'iata_code', 'gps_code', 'municipality', 'iso_country', 'latitude_deg', 'longitude_deg')