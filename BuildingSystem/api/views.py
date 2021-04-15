from django.shortcuts import render
from rest_framework import generics
from .models import Room,Building,Device
from .serializers import GetListBuildingSerializer,GetListDeviceSerializer, RoomSerializer,BuildingSerializer,DeviceSerializer
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

class GetDeviceList(generics.ListAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
   
    def list(self, request):
        queryset = self.get_queryset()
        serializer = DeviceSerializer(queryset, many = True)
        return Response(serializer.data)

class ListDeviceRoom(generics.RetrieveAPIView):
    queryset = Building.objects.all()
    serializer_class = GetListDeviceSerializer

    


    
    

    

