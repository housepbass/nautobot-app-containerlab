"""Serializers for Containerlab app."""
from rest_framework import serializers
from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin
from containerlab.models import Topology

class TopologySerializer(NautobotModelSerializer, TaggedModelSerializerMixin):
    """Topology serializer class"""

    class Meta:
        model = Topology
        fields = ["__all__"]
