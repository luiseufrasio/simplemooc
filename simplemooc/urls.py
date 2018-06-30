from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', include('core.urls', namespace='core')),
	path('contas/', include('accounts.urls', namespace='accounts')),
	path('cursos/', include('courses.urls', namespace='courses')),
	path('forum/', include('forum.urls', namespace='forum')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)