from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
from django.views import defaults as default_views
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from backend.users.views import UserViewSet,UserAPIViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomTokenObtainPairView
# from backend.compta.views import OrganizationViewSet
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserAPIViewSet)
# router.register("organizations", OrganizationViewSet)

app_name = "api"
urlpatterns = router.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Social Help API",
        default_version='v1.0',
        description="Social Help API documentation"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    # rest auth
    # path("auth/token", obtain_auth_token),
    url(r'^password-reset/$',
        TemplateView.as_view(template_name="password_reset.html"),
        name='password-reset'),
    # url(r'^password-reset/confirm/$',
    #     TemplateView.as_view(template_name="password_reset_confirm.html"),
    #     name='password-reset-confirm'),

    url(r'^password-change/$',
        TemplateView.as_view(template_name="password_change.html"),
        name='password-change'),

    # this url is used to generate email content

    # path("auth/", include("django.contrib.auth.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # swagger api documentation
    re_path(r'^swagger(?P<format>)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
