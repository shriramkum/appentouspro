from django.contrib import admin
from django.urls import path
from appentousapp.views import RegisterAPI
from appentousapp.views import Image_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register", RegisterAPI.as_view(), name="register_email"),
    path("api/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/image/", Image_view.as_view()),
]
