from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'epreuves', TestViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'sections-list', SectionViewList,basename='section-list')
router.register(r'send-email', SendEmailViewSet, basename='send-email')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('api/', include(router.urls)),
    re_path(r'^api/sections/(?P<query>[^/.]+)/$', SectionViewSet.as_view({'get': 'search_sections'}), name='search-sections'),
    re_path(r'^api/courses/(?P<query>[^/.]+)/$', CourseViewSet.as_view({'get': 'search_courses'}), name='search-courses'),
    re_path(r'^api/tests/(?P<query>[^/.]+)/$', TestViewSet.as_view({'get': 'search_tests'}), name='search-tests'),
]

