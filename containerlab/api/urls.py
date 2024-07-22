from django.urls import include, path
from nautobot.apps.api import OrderedDefaultRouter
from containerlab.api.views import TopologyViewSet

router = OrderedDefaultRouter()
router.register("topologies", TopologyViewSet)

urlpatterns = router.urls