from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/blog/', include('blogapp.urls', namespace='blog')),
    path('api/v1/diary/', include('diaryapp.urls', namespace='diary')),
    path('api/v1/todo/', include('todoapp.urls', namespace='todo')),
    path('api/v1/yellowpages/', include('yellowpagesapp.urls', namespace='yellowpages')),
    path('api/v1/publicapi/', include('publicapiapp.urls', namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
