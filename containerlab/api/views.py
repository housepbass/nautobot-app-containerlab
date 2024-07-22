from django.shortcuts import get_list_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from nautobot.apps.api import NautobotModelViewSet
from nautobot.extras.models import DynamicGroup

from containerlab import filters
from containerlab import models
from containerlab.api import serializers

class TopologyViewSet(NautobotModelViewSet):
    """Topology ViewSet."""
    queryset = models.Topology.objects.all()
    serializer_class = serializers.TopologySerializer
    filterset_class = filters.TopologyFilterSet