"""Containerlab Datasources."""
import os
import yaml
from nautobot.apps.datasources import DatasourceContent
from nautobot.extras.choices import LogLevelChoices

from containerlab.models import Topology


def refresh_git(repository_record, job_result, delete=False):  # pylint: disable=unused-argument
    """Callback for GitRepository updates on Containerlab repo."""
    topology_path = os.path.join(repository_record.filesystem_path)
    for folder in os.listdir(topology_path):
        topology_record = Topology.objects.filter(name=folder)
        if not topology_record:
            msg = f"Topology object {folder} doesn't exist."
            job_result.log(msg,
            level_choice=LogLevelChoices.LOG_INFO,
            )
            continue
        if topology_record.count() > 1:
            msg = f"Topology object {topology_record} returned more than one record."
            job_result.log(msg,
            level_choice=LogLevelChoices.LOG_INFO,
            )
            continue
        topology_record = topology_record[0]
        with open(os.path.join(topology_path, folder, f"{topology_record.name}.yml")) as fd:
            topology_data = fd.read()

        if topology_record.topology_file == topology_data:
            msg = "Topology already up to date."
        else:
            msg = "Topology has been updated."
            topology_record.topology_file = topology_data
            topology_record.validated_save()

        job_result.log(
            msg,
            obj=topology_record,
            level_choice=LogLevelChoices.LOG_INFO,
        )


    job_result.log(
        "Successfully pulled Containerlab Lab repo",
        level_choice=LogLevelChoices.LOG_INFO,
    )



datasource_contents = [
    (
        "extras.gitrepository",
        DatasourceContent(
            name="containerlab topologies",
            content_identifier="containerlab.topology",
            icon="mdi-flask-outline",
            callback=refresh_git,
        ),
    )
]