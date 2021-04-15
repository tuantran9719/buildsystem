from .views import (
    GetBuildingList,
    BuildingDetail,
    GetDeviceList,
    ListDeviceRoom
)
from django.urls import path

urlpatterns = [
    path('listbuilding/',GetBuildingList.as_view(), name = 'building_list'),    # API get list tòa nhà
    path('detailbuilding/<pk>',BuildingDetail.as_view(),name = 'building_detail'), # Get API thông tin chi tiết của tòa nhà như là mô tả,số phòng
    path('devicebuilding/<pk>',ListDeviceRoom.as_view(),name = 'device_list'),
    ]
