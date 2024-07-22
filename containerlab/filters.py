"""Filtersets for Containerlab App."""
from nautobot.apps.filters import (
    NautobotFilterSet,
    SearchFilter,
    TagFilter,
)
from .models import Topology

class TopologyFilterSet(NautobotFilterSet):
    """Filterset for Toplogy model."""
    q = SearchFilter(filter_predicates={"name": "icontains"})
    tags = TagFilter()

    class Meta:
        """Meta class."""
        model = Topology
        fields = ["name"]