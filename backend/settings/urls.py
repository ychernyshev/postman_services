from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(('accounts.urls', 'account'), namespace='account')),
    path('', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('simple_access/', include(('simple_user.urls', 'simple_user'), namespace='simple_user')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
