from rest_framework import routers
from .views import AboutViewSet

router = routers.SimpleRouter()
router.register('about', AboutViewSet, 'About')
urlpatterns = router.urls
