"""App declaration for containerlab."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class ContainerlabConfig(NautobotAppConfig):
    """App configuration for the containerlab app."""

    name = "containerlab"
    verbose_name = "Containerlab"
    version = __version__
    author = "Network to Code, LLC"
    description = "A Nautobot application for managing Containerlab topologies."
    base_url = "containerlab"
    required_settings = []
    min_version = "2.2.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = ContainerlabConfig  # pylint:disable=invalid-name
