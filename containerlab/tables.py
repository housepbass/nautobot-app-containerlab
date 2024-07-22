"""Views for Containerlab app."""
import django_tables2 as tables
from nautobot.apps.tables import BaseTable, ButtonsColumn, TagColumn, ToggleColumn
from .models import Topology

class TopologyTable(BaseTable):
    """Table for Topologies."""
    pk = ToggleColumn()
    name = tables.Column(linkify=True)
    dynamic_group = tables.Column(linkify=True, verbose_name="Dynamic Group")
    git_repository = tables.Column(linkify=True, verbose_name="Git Repository")
    tags = TagColumn(url_name="plugins:containerlab:topology_list")
    actions = ButtonsColumn(Topology)

    class Meta:
        """Meta class."""
        model = Topology
        fields = ("pk", "name", "dynamic_group", "git_repository", "tags", "actions")        
        