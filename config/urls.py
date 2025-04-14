from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('conversation/', include('conversation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)