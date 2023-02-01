from rest_framework import generics
from .serializers import permissionsSerializer
from .models import permissions


class permissionsList(generics.ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    # Serializer_class
    queryset = permissions.objects.all()
    serializer_class = permissionsSerializer


# The ThingDetail needs the same things
class permissionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = permissions.objects.all()
    serializer_class = permissionsSerializer
