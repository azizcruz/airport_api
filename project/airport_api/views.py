from django.shortcuts import render, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AirportInfo
from .serializers import AirportsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
import pandas as pd
# Create your views here.

class ListAirports(APIView):
    renderer_classes = (JSONRenderer,)
    def get(self, request, *args, **kwargs):
        # Fetch only the first 100 airports, due to the huge amount of data when fetching them all.
        airports = AirportInfo.objects.all()[:100]
        serializer = AirportsSerializer(airports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class IATA_search(APIView):
    renderer_classes = (JSONRenderer,)

    # Query airport information.
    def get_object(self, iata_code):
        try:
            return AirportInfo.objects.get(iata_code__iexact=iata_code)
        except AirportInfo.DoesNotExist:
            # This will raise 404 status code when not found with a proper message.
            raise Http404()

    
    def get(self, request, iata_code=None, name=None, *args, **kwargs):
        # When there is an iata_code sent with endpoint then get the airport that has the iata_code.
        if iata_code:
            airports = self.get_object(iata_code)
            serializer = AirportsSerializer(airports)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class NameFilter(APIView):
    renderer_classes = (JSONRenderer,)

    # Filter search by name all airports that contains name partially.
    def get(self, request, name=None, *args, **kwargs):
        if name:
            airports = AirportInfo.objects.filter(name__icontains=name)
            serializer = AirportsSerializer(airports, many=True)
            # When there is no data return a proper message and status code.
            if not serializer.data:
                return Response({"detail": "no results found."}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)

