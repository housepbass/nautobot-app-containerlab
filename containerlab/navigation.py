"""Navigation for menu items."""
from nautobot.apps.ui import NavMenuGroup, NavMenuItem, NavMenuTab

menu_items = (
    NavMenuTab(
        name="Containerlab",
        groups = (
            NavMenuGroup(
                name = "Containerlab",
                items=(
                    NavMenuItem(
                        link="plugins:containerlab:topology_list",
                        name="Topologies",
                        permissions=["ipam:view_topology"],
                        buttons=()
                    ),
                ),
            ),
        ),
    ),
)

