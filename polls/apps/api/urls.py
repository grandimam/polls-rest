from .views import UserViewSet
from .views import PollViewSet
from .views import QuestionViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'poll', PollViewSet, basename='poll')
router.register(r'question', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls))
]
