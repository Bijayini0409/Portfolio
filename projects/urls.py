from rest_framework import routers
from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register('project', ProjectViewSet, 'Project')
urlpatterns = router.urls