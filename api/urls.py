from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import ListUserView, FileUploadView, FileListView

router = DefaultRouter()
router.register(r'users', ListUserView, basename='user')
router.register(r'file-upload', FileUploadView, basename='file-upload')
router.register(r'file-list', FileListView, basename='file-list')


urlpatterns = [
    path('api/', include(router.urls)),
]

