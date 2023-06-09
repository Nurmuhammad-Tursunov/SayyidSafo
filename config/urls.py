from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Sayyid Safo API",
      default_version='v1',
      description="Ikki Buyuk Alloma",
      # terms_of_service="https://www.google.com/policies/terms/",
      # contact=openapi.Contact(email="contact@snippets.local"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="docs"),

    # topics
    path('topics/', TopicsListAPIView.as_view(), name='topics'),
    path('topics/<int:pk>/audios/', TopicAudiosApiView.as_view(), name='topic_audios'),

    # audios
    path('audios/', AudiosListAPIView.as_view(), name='audios'),
    path('audios/<int:pk>/', AudiosRetrieveAPIView.as_view(), name='audio'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

