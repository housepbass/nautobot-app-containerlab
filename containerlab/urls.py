"""URLs for Containerlab App."""
from django.urls import path
from nautobot.apps.urls import NautobotUIViewSetRouter
from . import views

app_name="containerlab"
router = NautobotUIViewSetRouter()
router.register("topologies", views.TopologyViewSet)


urlpatterns = router.urls