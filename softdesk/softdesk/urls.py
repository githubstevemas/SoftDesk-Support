from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet
from projects.views import ProjectsViewset, IssuesViewset, CommentsViewset

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users-list')
router.register('projects', ProjectsViewset, basename='projects-list')
router.register('issues', IssuesViewset, basename='issues-list')
router.register('comments', CommentsViewset, basename='comments-list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
