from rest_framework.routers import DefaultRouter
from user_app.views import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)
urlpatterns = router.urls