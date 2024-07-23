"""Models for Nautobot Containerlab."""
from django.db import models
from django.urls import reverse
from nautobot.apps.models import PrimaryModel

class Topology(PrimaryModel):
    """Model for Containerlab Topologies."""
    name = models.CharField(max_length=255, unique=True, help_text="Name of Containerlab Topology")
    dynamic_group = models.ForeignKey(
        to="extras.DynamicGroup",
        on_delete=models.CASCADE,
        related_name="containerlab_topologies",
        help_text="DynamicGroup from which to build the lab topology",
        blank=True,
        null=True,
    )
    topology_file = models.TextField(
        blank=True,
        null=True,
        help_text="Rendered topology file",
    )
    git_repository = models.ForeignKey(
        to="extras.GitRepository",
        on_delete=models.CASCADE,
        related_name="containerlab_topologies",
        limit_choices_to={"provided_contents__contains": "containerlab.topology"},
        help_text="Repository to store Containerlab Topology files",
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        """Return detail view for Topology."""
        return reverse("plugins:containerlab:topology", kwargs={"pk": self.pk})

    def __str__(self):
        """Stringify instance."""
        return self.name

    class Meta:
        """Meta class"""
        verbose_name = "Containerlab Topology"
        verbose_name_plural = "Containerlab Topologies"

