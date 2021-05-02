from rest_framework import routers
from contact.views import ContactmeViewSet

router = routers.DefaultRouter()
router.register('contacts', ContactmeViewSet, 'Contact')
urlpatterns = router.urls
