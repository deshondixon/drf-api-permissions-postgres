from rest_framework import serializers
from .models import permissions


class permissionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "owner", "name", "description", "created_at")
        model = permissions
