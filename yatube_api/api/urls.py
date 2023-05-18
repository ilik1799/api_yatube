from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, obtain_auth_token

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('posts/<int:post_id>/comments/', include(router.urls)),
    path('', include(router.urls)),
]
