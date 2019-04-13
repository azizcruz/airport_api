from rest_framework import serializers
from .models import AirportInfo

class AirportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportInfo
        fields = ('__all__')