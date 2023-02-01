from django.urls import path
from .views import permissionsList, permissionsDetail

urlpatterns = [
    path("", permissionsList.as_view(), name="permissions_list"),
    path("<int:pk>/", permissionsDetail.as_view(), name="permissions_detail"),
]