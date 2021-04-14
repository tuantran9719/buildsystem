from .views import (
    GetBuildingList,
    BuildingDetail,
)
from django.urls import path

urlpatterns = [
    path('listbuilding/',GetBuildingList.as_view(), name = 'building_list'),    # API get list tòa nhà
    path('detailbuilding/<pk>',BuildingDetail.as_view() , name = 'building_detail'), # Get API thông tin chi tiết của tòa nhà như là mô tả,số phòng
    ]