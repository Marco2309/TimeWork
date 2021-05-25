from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from task_app.views import TaskViewSet

router = DefaultRouter()
router.register('', TaskViewSet)
urlpatterns = router.urls
