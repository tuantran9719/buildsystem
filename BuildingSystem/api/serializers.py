from .models import Building,Room,Device
from rest_framework import serializers
from rest_framework.response import Response
from django.db.models import Count
from django.http import JsonResponse
import json 


class GetListBuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = ["name"]


class BuildingSerializer(serializers.ModelSerializer):
   
    count = serializers.SerializerMethodField()
    rooms = serializers.StringRelatedField(many=True)

    class Meta:
        model = Building
        fields = ("name","address","rooms","count")
    
    def get_count(self,obj):
        
        from .models import Room,Building
        count_room = Room.objects.filter(building=obj).count()
        return count_room


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"


class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Device
        fields = ["name"]

class GetListDeviceSerializer(serializers.ModelSerializer):
    Rooms = serializers.SerializerMethodField()

    class Meta:
        model = Building
        fields = ("name","address","Rooms")
    
    def get_Rooms(self,obj):
        devices = Device.objects.filter(room=obj)
        return DeviceSerializer(devices,many=True).data

