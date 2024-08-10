"""Containerlab Jobs."""
import re
import os
import yaml
from pathlib import Path

from nautobot.extras.jobs import get_task_logger
from nautobot.apps.jobs import Job, ObjectVar, register_jobs
from nautobot.apps.utils import render_jinja2
from nautobot.extras.models import JobResult, Job as extras_job
from containerlab.models import Topology

from git import Repo
# Temporary
from pathlib import Path

LOGGER = get_task_logger(__name__)


class GitRepo:
    """Object for interacting with git repository."""
    def __init__(self, repo_obj):
        """Init method."""
        self.path = repo_obj.filesystem_path
        # Needs to be updated
        self.token = Topology.objects.first().git_repository.secrets_group.secrets.first().get_value()
        self.url = re.sub("//", f"//{self.token}@", repo_obj.remote_url)
        self.branch = repo_obj.branch
        self.repo_obj = repo_obj

        if os.path.isdir(self.path):
            LOGGER.info("Git path `%s` exists, initiate", self.path)
            self.repo = Repo(path=self.path)
        else:
            LOGGER.info("Git path `%s` does not exists, clone", self.path)
            self.repo = Repo.clone_from(self.url, to_path=self.path)

        if self.url not in self.repo.remotes.origin.urls:
            LOGGER.info("URL `%s` was not currently set, setting", self.url)
            self.repo.remotes.origin.set_url(self.url)

    def commit_with_added(self, commit_description):
        """Make a force commit.

        Args:
            commit_description (str): the description of commit
        """
        LOGGER.info("Committing with message `%s`", commit_description)
        self.repo.git.add(self.repo.untracked_files)
        self.repo.git.add(update=True)
        self.repo.index.commit(commit_description)
        LOGGER.info("Commit completed")

    def push(self):
        """Push latest to the git repo."""
        LOGGER.debug("Push changes to repo")
        self.repo.remotes.origin.push()

class GenerateContainerlabTopology(Job):
    """Generate Containerlab Topology and push to git repo."""
    class Meta:
        name = "Generate Containerlab Topology"

    topology = ObjectVar(
        description="Containerlab Topology",
        model=Topology,
    )

    def run(self, topology):
        """Job run method."""
        self.logger.info("Topology Model.", extra={"object": topology})
        topology_repo = topology.git_repository
        repo = GitRepo(topology_repo)
        with open(os.path.join(os.path.dirname(__file__), "templates", "containerlab_topologies", "topologies.j2")) as handle:
            template = handle.read()
        topology_data = render_jinja2(template_code=template, context={"topology": topology})
        topology_path = f"/opt/nautobot/git/clab/{topology.name}"
        Path(topology_path).mkdir(parents=False, exist_ok=True)
        topology_data = "---\n" + yaml.dump(yaml.safe_load(topology_data))
        with open(f"{topology_path}/{topology.name}.yml", "w") as t_file:
            t_file.write(topology_data)
        repo.commit_with_added("Pushing to repo.")
        repo.push()
        self.launch_git_sync_job(topology_repo)

    def launch_git_sync_job(self, topology_repo):
        """Sync topology files from git repository."""
        job = extras_job.objects.get_for_class_path("nautobot.core.jobs.GitRepositorySync")
        try:
            job_result = JobResult.enqueue_job(
                job_model=job,
                user=self.user,
                repository=topology_repo.id,
            )
            self.logger.info("%s", job_result)
        except Exception as err:
            self.logger.exception(
                "Failed to launch GitSync with err %s.",
                err,
            )

register_jobs(GenerateContainerlabTopology)