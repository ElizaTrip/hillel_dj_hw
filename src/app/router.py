from rest_framework import routers

from app.views import PersonViewSet, GroupViewSet, SubjectViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet, basename='person')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'subject', SubjectViewSet, basename='subject')
