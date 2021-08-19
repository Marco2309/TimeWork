from rest_framework.routers import DefaultRouter
from user_app.views import UserViewSet, usernameOfEmail
from django.urls import path

router = DefaultRouter()
router.register('', UserViewSet)
urlpatterns = [path('searchUsername/', usernameOfEmail), ]
urlpatterns += router.urls