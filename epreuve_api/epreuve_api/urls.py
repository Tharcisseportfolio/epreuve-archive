from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView,EndpointListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # removing trailin slash
    path("admin/", admin.site.urls),
    path("api/user/register", CreateUserView.as_view(), name="register"),
    path("api/user/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/token", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("api/auth/", include("rest_framework.urls")),
    path('', EndpointListView.as_view(), name='endpoints'),
    path("", include("api.urls")),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)