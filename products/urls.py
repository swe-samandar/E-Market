from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),  # ✅ namespace berildi
    path('', include('main.urls', namespace='main')),          # (agar sizda `main` app ham bo‘lsa)
]
