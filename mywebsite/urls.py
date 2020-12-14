from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('blog/', include('blogapp.urls', namespace='blog')),
    path('diary/', include('diaryapp.urls', namespace='diary')),
    path('todo/', include('todoapp.urls', namespace='todo')),
    path('yellowpages/', include('yellowpagesapp.urls', namespace='yellowpages')),
    path('portofolio/', include('portofolioapp.urls', namespace='portofolio'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
