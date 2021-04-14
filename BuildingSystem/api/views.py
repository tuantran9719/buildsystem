from django.shortcuts import render
from rest_framework import generics
from .models import Room,Building,Device
from .serializers import GetListBuildingSerializer,RoomSerializer,RoomSerializer,BuildingSerializer
from rest_framework.response import Response
from django.db.models import Count



class GetBuildingList(generics.ListAPIView):
    queryset = Building.objects.all()
    serializer_class = GetListBuildingSerializer
   
    def list(self, request):
        queryset = self.get_queryset()
        serializer = GetListBuildingSerializer(queryset, many = True)
        return Response(serializer.data)

class BuildingDetail(generics.RetrieveAPIView):
    queryset  = Building.objects.all()
    serializer_class = BuildingSerializer

    
    
    

    

