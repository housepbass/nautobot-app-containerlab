from django import forms
from nautobot.apps.forms import (
    NautobotModelForm, DynamicModelChoiceField
)
from nautobot.extras.models import DynamicGroup
from nautobot.extras.models.datasources import GitRepository
from .models import Topology

class TopologyForm(NautobotModelForm):
    """Form for Topology creation/edits."""
    dynamic_group = DynamicModelChoiceField(
        queryset=DynamicGroup.objects.all(), label="Dynamic Group"
    )
    git_repository = DynamicModelChoiceField(
        queryset=GitRepository.objects.filter(provided_contents__contains="containerlab.topology"), label="Git Repository"
    )
    class Meta:
        """Meta class."""
        model = Topology
        fields = ["name", "dynamic_group", "git_repository"]