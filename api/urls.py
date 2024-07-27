from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import *
router = DefaultRouter()
router.register(r'file-upload', FileUploadView, basename='file-upload')
router.register(r'file-list', FileListView, basename='file-list')
router.register(r'epreuves',EpreuveView,basename='epreuves')
router.register(r'courses',CourseView,basename='courses')
router.register(r'grades',GradeView,basename='grades')
router.register(r'sections',SectionView,basename='sections')

#the viewset allows id access easily////

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/9/courses/', NinthGradeCoursesView.as_view(), name='9-courses/'),
    path('api/3/courses/', ThirdGradeCoursesView.as_view(), name='3-courses/'),
    path('api/users/',ListUserView.as_view(),name='users'),
    path('api/epreuve-list',EpreuveListView.as_view(),name='epreuve-list')

]

