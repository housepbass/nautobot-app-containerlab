"""Views for Containerlab App."""
from nautobot.apps import views
from nautobot.extras.models import DynamicGroup
from . import forms, filters, models, tables
from .api import serializers

class TopologyViewSet(views.NautobotUIViewSet):
    """View for Topology."""
    filterset_class = filters.TopologyFilterSet
    form_class = forms.TopologyForm
    lookup_field = "pk"
    queryset = models.Topology.objects.all()
    serializer_class = serializers.TopologySerializer
    table_class = tables.TopologyTable
