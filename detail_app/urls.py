from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from detail_app.views import DetailViewSet

router = DefaultRouter()
router.register('', DetailViewSet)
urlpatterns = router.urls
