from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView

from comments.views import CommentsViewset
from issues.views import IssuesViewset
from users.views import UserViewSet
from projects.views import ProjectsViewset

router = routers.SimpleRouter()
router.register('users', UserViewSet, basename='users-list')
router.register('projects', ProjectsViewset, basename='projects-list')
router.register('comments', CommentsViewset, basename='comments-list')
router.register(r'projects/(?P<project_id>\d+)/issues', IssuesViewset,
                basename='project-issues')
router.register(
    r'projects/(?P<project_id>\d+)/issues/(?P<issue_id>\d+)/comments',
    CommentsViewset, basename='issue-comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/connection/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/refresh-token/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
